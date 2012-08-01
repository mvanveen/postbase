import argparse

from config import Configuration
from postbin import app

PORT_STR = 'Port number to listen on'
FILENAME_STR = 'filename of the database to write to'
HOSTNAME_STR = 'Hostname to listen on'

def get_cmd_args():
  conf = Configuration()
  parser = argparse.ArgumentParser(description=conf.description)
  parser.add_argument('--port', metavar='p', type=int, help=PORT_STR)
  parser.add_argument('--filename', metavar='f', type=str, help=FILENAME_STR)
  parser.add_argument('--hostname', type=str, default='', help=HOSTNAME_STR)

  return parser.parse_args()

if __name__ == "__main__":
  conf = Configuration(parsed_config=get_cmd_args())
  app.run(port=conf.port, host=conf.hostname)
