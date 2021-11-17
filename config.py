import logging
from os import environ

LOGGING_LEVEL = logging.INFO
LOGGING_HANDLER = logging.StreamHandler()
LOGGING_FORMATTER = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')


NODE_NAME = environ.get('NODE_NAME', 'node')
POD_NAMESPACE = environ.get('POD_NAMESPACE', 'namespace')
POD_NAME = environ.get('POD_NAME', 'pod')
POD_IP = environ.get('POD_IP', 'namespace')
