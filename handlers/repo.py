#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from github import Github

from handlers.base import BaseHandler

ACCESS_TOKEN = 'c9005d9c52b7b331d993376f9c650583e5bc3932'


class ReposHandler(BaseHandler):
    def get(self, user, repo_name):
        client = Github(ACCESS_TOKEN, per_page=20)
        user = client.get_user(user)
        repo = user.get_repo(repo_name)

        stargazers = [s.name for s in repo.get_stargazers()]

        self.write(stargazers)

