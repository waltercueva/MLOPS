from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, configure_mappers
from sqlalchemy.ext.declarative import declarative_base
import os


Base = declarative_base()

def init_db(database_uri):
    """ Database Initialization
    """
    engine = create_engine(database_uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(
        autocommit=False, autoflush=False, bind=engine))
    Base.query = db_session.query_property()

    from . import congress
    from . import academic
    from . import experience
    from . import law
    from . import topic
    # from . import congress_law

    configure_mappers()
    Base.metadata.create_all(bind=engine)
    return db_session


def database_config():
    user = os.getenv('DATABASE_USER', 'root')
    password = os.getenv('DATABASE_PASSWORD', 'root')
    host = os.getenv('DATABASE_HOST', '127.0.0.1')
    port = os.getenv('DATABASE_PORT', '3306')
    database = os.getenv('DATABASE_NAME', 'admin')
    db_session = init_db('mysql+pymysql://%s:%s@%s:%s/%s' %
                         (user, password, host, port, database))

    return db_session
