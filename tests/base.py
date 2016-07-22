#!/usr/bin/env python
from tornado.testing import AsyncHTTPSTestCase
import tornado.web

from urls import url_pattern
from settings import settings
from models import conn


class BaseHTTPTestCase(AsyncHTTPSTestCase):
    def get_app(self):
        return tornado.web.Application(url_pattern, **settings)

    def tearDown(self):
        super(AsyncHTTPSTestCase, self).tearDown()
        conn.drop_database(settings['mongo']['db'])

