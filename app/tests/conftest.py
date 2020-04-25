import pytest
from alembic import command
from alembic.config import Config as AlembicConfig, Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from testcontainers.postgres import PostgresContainer


Session = sessionmaker()

target_metadata = None

@pytest.fixture(scope='session')
def use_container_engine():
    postgres_container = PostgresContainer("postgres:10.12")
    with postgres_container as postgres:

        engine = create_engine(postgres.get_connection_url())

        with engine.connect() as connection:
            alembic_cfg = Config("alembic.ini")
            alembic_cfg.attributes['sqlalchemy.url'] = postgres.get_connection_url()
            command.upgrade(alembic_cfg, "head")

            yield connection
            connection.close()

@pytest.fixture(scope='function')
def database_session(use_container_engine):
    transaction = use_container_engine.begin()
    session = Session(bind=use_container_engine)

    yield session

    session.close()
    transaction.rollback()
