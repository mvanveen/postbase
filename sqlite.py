from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

import config

Base  = declarative_base()

SQLITE_PATH = 'sqlite:///' + config.get_sqlite_filename()

class Post(Base):
  """Represents a UNIX Alias found from Github"""
  __tablename__ = 'postdata'

  id   = Column(Integer, primary_key=True)
  time = Column(Float, nullable=False)
  url  = Column(String(255), nullable=False)
  data = Column(Text, nullable=False)
  query = Column(Text, nullable=False)

  def __init__(self, *args):
    super(Post,self).__init__ ()
    self.url, self.time, self.data, self.query = args

  def __repr__(self):
    return 'Post(%s: %s [%s])' % (self.id, self.url, self.time)


def create_database(filename=None):
  if not filename:
    filename = SQLITE_PATH
  return create_engine(filename, echo=True)


def get_database(engine=None, filename=None):
  if not engine:
    engine = create_database(filename=filename)
    Base.metadata.create_all(engine)
  return engine

if __name__ == '__main__':
  get_database()
