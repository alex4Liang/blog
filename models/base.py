#!/usr/bin/env python
from pymongo import MongoClient

from settings import settings


client = MongoClient(settings['mongo']['address'], settings['mongo']['port'])
db = client[settings['mongo']['db']]
