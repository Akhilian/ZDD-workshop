import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from testcontainers.postgres import PostgresContainer

from presentation.api import api
from presentation.connection import db

Session = sessionmaker()

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
