#encoding: utf-8
import os

# Defaults
SQLITE_FILENAME_DEFAULT = 'requests.sql'
HTTP_PORT_DEFAULT = '80'

# Help strings
PORT_STR = 'Port number to listen on'
FILENAME_STR = 'filename of the database to write to'
HOSTNAME_STR = 'Hostname to listen on'


class Configuration(object):
  """Sets and gets configuration options for the app"""

  def __init__(self, parsed_config=None):
    self._parsed_config = parsed_config

  @property
  def sqlite_filename(self):
   return (
     self._parsed_config.filename or
     os.environ.get('POSTBIN_SQLITE_FILENAME') or
     SQLITE_FILENAME_DEFAULT
   )

  @property
  def port(self):
    return (
      self._parsed_config.port or
      os.environ.get('POSTBIN_HTTP_PORT') or
      HTTP_PORT_DEFAULT
    )

  @property
  def hostname(self):
    return self._parsed_config.hostname or '0.0.0.0'

  @property
  def description(self):
    return 'SQLite-hosted HTTP Request Logging for Whoever™'


def get_cmd_args():
  conf = Configuration()
  parser = argparse.ArgumentParser(description=conf.description)
  parser.add_argument('--port', metavar='p', type=int, help=PORT_STR)
  parser.add_argument('--filename', metavar='f', type=str, help=FILENAME_STR)
  parser.add_argument('--hostname', type=str, default='', help=HOSTNAME_STR)

  return parser.parse_args()


def get_configuration():
  return Configuration(parsed_config=get_cmd_args())

import argparse

