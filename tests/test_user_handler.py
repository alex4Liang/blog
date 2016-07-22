#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json

from tests.base import BaseHTTPTestCase


class UserHandlerTestCase(BaseHTTPTestCase):
    def test_post_new_user(self):
        params = {'username': 'new', 'password': 'password'}
        response = self.fetch('/users', method='POST', body=json.dumps(params))
        self.assertEqual(response.code, 200)

        response_data = json.loads(response.body.decode('utf-8'))
        self.assertIsNotNone(response_data)

