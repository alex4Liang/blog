#!/usr/bin/env python
from mongoengine import (connect, Document)

from settings import settings

conn = connect(
        settings['mongo']['db'],
        host=settings['mongo']['address'],
        port=settings['mongo']['port']
)


class BaseDocument(Document):
    meta = {
        'abstract': True
    }

    def to_dict(self):
        result = {}
        for field in self._fields.keys():
            result[field] = getattr(self, field)

            if field == 'id':
                result[field] = str(result[field])

        return result
