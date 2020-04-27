from contextlib import contextmanager
from unittest.mock import patch

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from testcontainers.postgres import PostgresContainer

from application.api import api
from application.connection import db

target_metadata = None


@pytest.fixture(scope='session')
def with_database():
    postgres_container = PostgresContainer("postgres:10.12")
    with postgres_container as postgres:
        db_url = postgres.get_connection_url()

        alembic_cfg = Config("alembic.ini")
        alembic_cfg.attributes['sqlalchemy.url'] = db_url
        command.upgrade(alembic_cfg, "head")

        yield db_url


@pytest.fixture(scope='session')
def with_database():
    postgres_container = PostgresContainer("postgres:10.12")
    with postgres_container as postgres:
        db_url = postgres.get_connection_url()

        alembic_cfg = Config("alembic.ini")
        alembic_cfg.attributes['sqlalchemy.url'] = db_url
        command.upgrade(alembic_cfg, "head")

        yield db_url


@pytest.fixture(scope='function')
def use_connection(with_database):
    print(with_database)
    # engine = create_engine(with_database)
    # api.config['TESTING'] = True
    # api.config['SQLALCHEMY_DATABASE_URI'] = with_database
    # db.init_app(api)
    #
    # with engine.connect() as connection:
    #     alembic_cfg = Config("alembic.ini")
    #     alembic_cfg.attributes['sqlalchemy.url'] = with_database
    #     command.upgrade(alembic_cfg, "head")
    #
    #     yield connection
    #
    #     connection.close()


# @pytest.fixture(scope='session')
# def use_container_engine():
#     postgres_container = PostgresContainer("postgres:10.12")
#     with postgres_container as postgres:
#         db_url = postgres.get_connection_url()
#         engine = create_engine(db_url)
#         api.config['TESTING'] = True
#         api.config['SQLALCHEMY_DATABASE_URI'] = db_url
#         db.init_app(api)
#
#         with engine.connect() as connection:
#             alembic_cfg = Config("alembic.ini")
#             alembic_cfg.attributes['sqlalchemy.url'] = db_url
#             command.upgrade(alembic_cfg, "head")
#
#             yield connection
#
#             connection.close()

#
# @pytest.fixture(scope='function')
# def database_session(use_container_engine):
#     transaction = use_container_engine.begin()
#     session = Session(bind=use_container_engine)
#
#     yield session
#
#     session.close()
#     transaction.rollback()
#
#
# @pytest.fixture(scope='function')
# def integration_testing(database_session):
#     with api.test_client() as http_client:
#         return http_client


@pytest.fixture(scope='function')
def with_client(with_database):
    api.config['TESTING'] = True
    # api.config['SQLALCHEMY_DATABASE_URI'] = with_database
    with api.test_client() as http_client:
        return http_client


# #####################################################################
# database -> url -> connection -> session -> api -> client

@pytest.fixture(scope='session')
def use_container_engine():
    postgres_container = PostgresContainer("postgres:10.12")
    with postgres_container as postgres:
        db_url = postgres.get_connection_url()
        engine = create_engine(db_url)

        with engine.connect() as connection:
            alembic_cfg = Config("alembic.ini")
            alembic_cfg.attributes['sqlalchemy.url'] = db_url
            command.upgrade(alembic_cfg, "head")

            connection.close()

            yield db_url


Session = sessionmaker()


@pytest.fixture(scope='session')
def get_db_connection(use_container_engine):
    engine = create_engine(use_container_engine)

    with engine.connect() as connection:
        yield connection
        connection.close()


@pytest.fixture(scope='function')
def database_session(get_db_connection):
    transaction = get_db_connection.begin()
    session = Session(bind=get_db_connection)

    yield session

    session.close()
    transaction.rollback()



@pytest.fixture(scope='function')
def end_to_end(database_session, use_container_engine):
    api.config['TESTING'] = True
    api.config['SQLALCHEMY_DATABASE_URI'] = use_container_engine
    api.app_context().push()

    @api.teardown_request
    def teardown_request(exception):
        db.session.rollback()

    with api.test_client() as http_client:
        yield http_client
