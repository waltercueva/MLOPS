from flask import g
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, configure_mappers
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

def init_db(database_uri):
    """ Database Initialization
    """
    engine = create_engine(database_uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    Base.query = db_session.query_property()

    from . import congress
    from . import academic
    from . import experience
    from . import law
    from . import topic

    configure_mappers()
    Base.metadata.create_all(bind=engine)
    return db_session

def database_config(app):
    db_session = init_db('mysql+pymysql://root:root@35.237.141.25:3306/admin')
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    @app.before_request
    def setup_db():
        g.db = db_session
