#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from models.base_model import BaseModel
import datetime

class RecommentInfo(BaseModel):
    __table__ = "recomment"
    __invalid__ = {"media_type":{"_name":"媒体类型", type:int, "min":0, "max":4}\
        , "media_id":{"_name":"媒体唯一ID", type:str, "min_length":0, "max_length":100}\
        , "media_name":{"_name":"媒体名称", type:str,  "min_length":0, "max_length":100}\
        , "media_tags":{"_name":"媒体类型", type:str,  "min_length":0, "max_length":100}\
        , "media_image_path":{"_name":"媒体图片地址", type:str,  "min_length":0, "max_length":100}}

    __msg__ = {
        "type": "%s类型错误",
        "max_length": "%s长度太长",
        "min_length": "%s长度太短",
        "min": "% 数据太小",
        "max": "% 数据太大"
    }#和__invalid__ 数据错误对应
    error_msg = ""
