import os

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///flask_app.db')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))

# define the database
engine = create_engine(DATABASE_URL)

# creates all tables in the database
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """
    When accessing the database, use the following syntax:
        with session_scope() as db_session:
            db_session.query(...)

    :return: the session for accessing the database
    """
    session = DBSession()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def add_user(name, email):
    with session_scope() as db_session:
        db_session.add(User(name=name, email=email))


def get_all_users():
    with session_scope() as db_session:
        users = db_session.query(User).all()
        db_session.expunge_all()
        return users
