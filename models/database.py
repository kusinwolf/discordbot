# Third party imports
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import sqlalchemy

# Application imports
import config


def load_db(config):
    """
    Creates a SQLAlchemy session to be used by the controllers

    :param config: Configuration information provided by :meth:load_config
    :type config: dict
    :returns: SQLAlchemy Session
    :rtype: sqlalchemy.orm.session.Session
    """
    engine = sqlalchemy.create_engine(
        config["postgresql"]["sqlalchemy_uri"].format(**config["postgresql"])
    )
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    return Session()


def init_db():
    """
    Creates the tables in the database if they don't exist.
    Currently requires each model to be imported to ensure they're loaded
    before the tables are created

    :returns: Nothing
    :rtype: None
    """

    # Prevent circular imports
    # TODO: Convert this to autowalker
    from models import feeds  # noqa: F401

    Base.metadata.create_all(bind=engine)


engine = sqlalchemy.create_engine(
    config.postgresql["sqlalchemy_uri"].format(**config.postgresql)
)
session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = session.query_property()
