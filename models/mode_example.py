#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from models.base_model import BaseModel
class Example(BaseModel):
    __table__ = "example"
    __invalid__ = {"test":{ "_name":"xx"\
        , "type":str\
        , "max_length":21\
        , "min_length":1}}
    __msg__ = {
        "type": "%s类型错误",
        "max_length": "%s长度太长",
        "min_length": "%s长度太短"
    }#和__invalid__ 数据错误对应
    error_msg = ""