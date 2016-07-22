#!/usr/bin/env python
from models import User
from handlers.base import BaseHandler


class UsersHandler(BaseHandler):
    def get(self):
        self.write('What is ur name?')
        pass

    def post(self):
        user = User.add_user(
                self.body.get('username', ''), self.body.get('password', '')
        )
        self.write(user)
