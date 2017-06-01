#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import tornado
import tornado.web
import tornado.httpserver
import tornado.autoreload
import tornado.ioloop
from tornado.options import define, options
from etc import etc
from urls import urls

import os.path
import configparser

from motor import MotorClient

define("port", default=8004, help="run on the given port", type=int)

class MediaApp(tornado.web.Application):
    def __init__(self):
        handler = urls
        settings = etc
        session_settings = dict(
            driver="redis",
            driver_settings=dict(
                host='47.93.23.32',
                port=11211,
                db=0,
                password="yuetianle",
                max_connections=1024,
            ),
            sid_name='3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc',  # default is msid.
            session_lifetime=30*60,  # default is 1200 seconds.
            force_persistence=True,
        )
        settings.update(session=session_settings)
        tornado.web.Application.__init__(self, handler, **settings)

def start_media_app(db_config_name):
    if os.path.exists(db_config_name) and os.path.isfile(db_config_name):
        config = configparser.ConfigParser()
        config.read(db_config_name)
    mongo_url = config.get('mongodb', 'config')
    mongo_db_name = config.get('mongodb', 'db')
    client = MotorClient(mongo_url)
    db = client[mongo_db_name]
    etc.update({"database": db})
    server = tornado.httpserver.HTTPServer(MediaApp())
    server.listen(options.port)
    tornado.autoreload.start(tornado.ioloop.IOLoop.instance())
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    db_name = "mongodb.ini"
    start_media_app(db_name)


