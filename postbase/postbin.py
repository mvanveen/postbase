import datetime
import json
import logging
import time

from deps.bottle import Bottle, request
from sqlalchemy.orm import Session, sessionmaker

import config
from sqlite import Post, get_database

__author__ = 'Michael Van Veen (michael@mvanveen.net)'

app = Bottle()
Session = sessionmaker(bind=get_database())

@app.post('/<url>')
@app.get('/<url>')
@app.get('/')
@app.post('/')
def get_post(url=''):
  session = Session()

  logging.info('retrieved url: / %s', url)

  p = Post(
    '/' + url,
    time.mktime(datetime.datetime.utcnow().timetuple()),
    request.body.read(),
    json.dumps(dict(request.query))
  )
  session.add(p)

  logging.info(p)

  try:
    session.commit()
  except Exception, e:
    logging.exception(e)
    session.rollback()

  return dict(request.forms)
