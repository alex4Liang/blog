#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from passlib.hash import md5_crypt
from models import db


class User(object):
    collection = db['user']

    @classmethod
    def add_user(cls, username, password):
        hashed_password = md5_crypt.encrypt(password)

        user = cls.collection.insert({
            username: username, password: hashed_password
        })

        return cls.collection.find_one({'_id': user})
