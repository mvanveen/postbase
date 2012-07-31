import json
import sys

from sqlalchemy import create_engine
from sqlite import Post, get_database
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///' + sys.argv[1], echo=True)

Session = sessionmaker(engine)
session = Session()

items = session.query(Post).all()

print json.loads(json.loads(items[3].data).keys()[0])
