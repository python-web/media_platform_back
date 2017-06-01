#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from models.base_model import BaseModel
try:
    type(u"a") is unicode
except:
    # PY3
    unicode = str
class UserModel(BaseModel):
    __table__ = "member"
    __invalid__ = {
        "username": {
            "_name": "用户名",
            "_need": True,
            "type": unicode,
            "max_length": 36,
            "min_length": 1,
        },
        "password": {
            "_name": "password",
            "type": unicode,
            "max_length": 64,
        },
        "power": {
            "_name": "power",
            "type": int,
            "max": 6,
        },
    }
    __msg__ = {
        "type": "%s类型错误",
        "max_length": "%s长度太长",
        "min_length": "%s长度太短",
        "max": "%s过大",
        "min": "%s过小",
        "email": "%s格式错误",
        "number": "%s必须是数字",
        "url": "%s格式错误",
        "pattern": "%s格式错误"
    }
    error_msg = ""
