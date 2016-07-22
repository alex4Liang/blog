#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
from bson import ObjectId

from models.user import User

from tests.base import BaseHTTPTestCase


class UserHandlerTestCase(BaseHTTPTestCase):
    def test_found_page(self):
        response = self.fetch('/users')
        self.assertEqual(response.code, 200)

    def test_post_new_user(self):
        params = {'username': 'new', 'password': 'password'}
        response = self.fetch('/users', method='POST', body=json.dumps(params))
        self.assertEqual(response.code, 200)

        response_data = json.loads(response.body.decode('utf-8'))
        user = User.collection.find_one({
            '_id': ObjectId(response_data['_id'])
        })
        self.assertIsNotNone(user)

