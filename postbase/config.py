import os

SQLITE_FILENAME_DEFAULT = 'requests.sql'
HTTP_PORT_DEFAULT = '80'

def get_sqlite_filename():
  return os.environ.get('POSTBIN_SQLITE_FILENAME') or SQLITE_FILENAME_DEFAULT

def get_port():
  return os.environ.get('POSTBIN_HTTP_PORT') or HTTP_PORT_DEFAULT

def get_hostname():
  return '0.0.0.0'
