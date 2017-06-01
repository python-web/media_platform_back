#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import json
from utils.common_data import UserType, UserInfoName, UserInfoTableName, CurrentUserName
from torndsession.sessionhandler import SessionBaseHandler

class RenderInfo():
    def __init__(self, content):
        if content and isinstance(content, dict):
            for key, item in content.items():
                if not hasattr(self, key):
                    setattr(self, key, item)

class BaseHandler(SessionBaseHandler):
    def initialize(self):
        self.db = self.settings.get("database")
    def prepare(self):
        self.power = UserType.Guest

        #检测是否登录
    def check_login(self):
        try:
            assert type(self.current_user) is dict
            assert self.current_user.has_key(UserInfoTableName.UserName)
        except AssertionError:
            if self.get_cookie(UserInfoName):
                self.clear_cookie(UserInfoName)
            if self.request.path == "/":
                self.redirect("/home")
    def set_session(self, user):
        try:
            assert ("_id" in user and UserInfoTableName.UserName.value in user)
            if isinstance(user, dict):
                session = user
                self.session[CurrentUserName] = session
                print("session:{0}".format(self.session[CurrentUserName]))
                return session
        except:
            return None


    def get_current_user(self):
        try:
            # user = self.session.get(CurrentUserName)
            user = self.session[CurrentUserName]
            if not user and self.get_cookie(UserInfoName):
                scookie = self.get_secure_cookie(UserInfoName)
                user = json.loads(scookie)
                if not self.set_seesion(user):
                    assert False
        except:
            user = None
        return user
