#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import tornado.web
import tornado.gen
import json
from handlers.base_handler import BaseHandler
from enum import Enum

class LoginInfoName(Enum):
    UserName = "name"
    Password = "password"
    Power = "power"

class LoginHandler(BaseHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        self.render("login.html")

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        user_name = self.get_body_argument(LoginInfoName.UserName.value, None)
        password = self.get_body_argument(LoginInfoName.Password.value, None)
        power = self.get_body_argument(LoginInfoName.Power.value, None)
        remeber = self.get_body_argument("remeber", None)
        if user_name and password and power is not None:
            user = yield self.db.user.find_one({LoginInfoName.UserName.value:user_name})
            #检查密码是否正确 后续进行加密
            if user.get(LoginInfoName.Password.value) == password:
                checked = True
            else:
                checked = False
            if user and checked:
                session = self.set_session(user)
                self.current_user = session
                if remeber == "on":
                    cookie_json = json.dumps(session)
                    self.set_secure_cookie("user_info", cookie_json, expires_days=30, httponly=True)
                print("session:{0}".format(self.session))
                self.redirect("/")
            else:
                self.redirect("/login")
        else:
            return self.send_error()

    def check_xsrf_cookie(self):
        xrsf_cookie = self.get_cookie("_xrsf", None)
        print("xrsf:{0}".format(xrsf_cookie))
