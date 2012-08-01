from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

from config import get_configuration

Base  = declarative_base()
config = get_configuration()

SQLITE_PATH = 'sqlite:///' + config.sqlite_filename

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


def get_database(engine=None, filename=None):
  filename = filename or SQLITE_PATH
  if not engine:
    engine = create_engine(
      filename,
      echo=True
    )
    Base.metadata.create_all(engine)
  return engine

if __name__ == '__main__':
  get_database()
