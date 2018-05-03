# -*- coding: utf-8 -*-

import os
import sys
import json
import logging
import datetime
import tornado.web
import tornado.escape
import candax.rest as rest
from candax.auth import jwtauth
import uuid

LOGGER = logging.getLogger(__name__)
bucket = 'alarms'
bucket_a = 'administrators'


@jwtauth
class MainHandler(rest.BaseHandler):
    def initialize(self, db=None):
        self.db = db

    @tornado.gen.coroutine
    def get(self, _id=None):
        if _id is None:
            #objs = yield self.application.db.get_all(bucket)
            print('jkdasjdklsadja')
        else:
            data_admin = yield self.application.db.get(bucket_a, _id)
            s = data_admin['res_unit']
            objs = yield self.application.db.get_all_user(bucket, s, 'Admin')
        # self.set_status(403)
        objs = json.dumps(objs)
        self.set_header('Content-Type', 'text/javascript;charset=utf-8')
        self.write(objs)

    # @tornado.gen.coroutine
    # def post(self, *args):
    #     k = str(uuid.uuid1().int)
    #     self.json_args['key'] = k
    #     _id = yield self.application.db.insert(bucket, self.json_args)
    #     # if self.json_args is not None:
    #     #   ret, perm, email, _type = yield self.authenticate('administrador')
    #     #   if perm:
    #     #     edgarin= aerolinea.Aerolinea.from_json(self.json_args)
    #     #     response= yield tm.registrar_aerolinea(edgarin)
    #     #     self.set_status(201)
    #     #     response = response.json()
    #     #   else:
    #     #     response = tornado.escape.json_encode(ret)
    #     #     self.set_status(403)
    #     # else:
    #     #   self.set_status(400)
    #     #   response = "Error: Content-Type must be application/json"
    #     # response = "Unknown"
    #     self.set_header('Content-Type', 'text/javascript;charset=utf-8')
    #     self.write(_id)

    # @tornado.gen.coroutine
    # def put(self, *args):
    #     # print("MSG: {0}".format(self.application.db is None))
    #     #bucket = 'test'
    #     objs = yield self.application.db.update(bucket, self.json_args)
    #     # self.set_status(403)
    #     print(objs)
    #     objs = json.dumps(objs)
    #     self.set_header('Content-Type', 'text/javascript;charset=utf-8')
    #     self.write(objs)
    #
    # @tornado.gen.coroutine
    # def delete(self, _, _id=None):
    #     #bucket = 'test'
    #     print(_id)
    #     if _id is None:
    #         #objs = yield self.application.db.get_all(bucket)
    #         print('no hay naditaaaaa')
    #     else:
    #         objs = yield self.application.db.delete(bucket, _id)
    #     # self.set_status(403)
    #     objs = json.dumps(objs)
    #     self.set_header('Content-Type', 'text/javascript;charset=utf-8')
    #     self.write(objs)