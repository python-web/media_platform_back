#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from handlers.base_handler import BaseHandler
import tornado.web

class ApiHomeHandler(BaseHandler):

    # @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("home.html")
        # self.render("index.html")
