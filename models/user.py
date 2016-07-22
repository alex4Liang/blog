#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from passlib.hash import md5_crypt
from mongoengine import StringField

from models.base import BaseDocument


class User(BaseDocument):
    username = StringField(required=True, unique=True)
    password = StringField()

    @classmethod
    def add_user(cls, username, password):
        hashed_password = md5_crypt.encrypt(password)

        user = User(username=username, password=hashed_password)
        user.save()
        return user.to_dict()
