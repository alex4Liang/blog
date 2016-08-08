#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from handlers.user import UsersHandler
from handlers.repo import ReposHandler

url_pattern = [
    # (r'/users', UsersHandler),
    (r'/(?P<user>[\w\-_]+)/(?P<repo_name>[\w_\-]+)', ReposHandler),
]
