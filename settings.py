#!/usr/bin/env python
import os
import yaml
import logging
from tornado.options import define


environment = os.environ.get('ENV', 'development')
config_file = '{directory}/config/{filename}.yml'.format(
        directory=os.getcwd(), filename=environment
)

settings = {}
try:
    with open(config_file, 'r') as f:
        settings = yaml.load(f.read())
except FileNotFoundError as e:
    logging.error(e)
    logging.error('ENV not set properly.')

define('port', default=8888, help='run on the given port', type=int)
