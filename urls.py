#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from handlers.user import UsersHandler

url_pattern = [
    (r'/users', UsersHandler),
]
