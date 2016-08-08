#!/usr/bin/env python
import json

import tornado.web
import tornado.escape


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.body = tornado.escape.json_decode(self.request.body) \
            if self.request.body else None

    def write(self, chunk, **kwargs):
        """
        write stream to client
            - 如果 _finished, 则直接返回
            - MessageCode 定制化
            - chunk to json
            - force finish immediately after write
        :param chunk:
        :param kwargs:
        :return:
        """
        if self._finished:
            return
        if chunk is None:
            self.finish()
            return
        # if isinstance(chunk, message_code.MessageCode):
        #     self.set_status(chunk.status_code)
        #     chunk = chunk.to_dict()
        if isinstance(chunk, dict):
            # 过滤为None的字段信息
            chunk = {k: v for k, v in chunk.items() if v is not None}
        if isinstance(chunk, (dict, list, tuple)):
            chunk = json.dumps(chunk, **kwargs)
            self.set_header("Content-Type", "application/json; charset=UTF-8")
        super(BaseHandler, self).write(chunk)
        self.finish()
