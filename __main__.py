import config
from postbin import app

if __name__ == "__main__":
  app.run(port=config.get_port(), host=config.get_hostname())
