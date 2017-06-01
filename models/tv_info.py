#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime
from models.base_model import BaseModel
class TV(BaseModel):
    """
    tv_play_url: 集数:播放地址[list]内容 media_type url 清晰度
    example: 1:[["video/mpr", "http::fjsdfl.mp4", "高清"]]
    """
    __table__ = "tv"
    __invalid__ = {"tv_id":{"_name":"电视ID", type:str, "max_length":100, "min_length":0} \
        , "tv_name":{"_name":"电视名称", type:str, "max_length":50, "min_length":0} \
        , "tv_image_path":{"_name":"电视截图地址", type:str, "max_length":320, "min_length":0} \
        , "tv_born":{"_name":"电视上映日期", type:datetime} \
        , "tv_categeroy":{"_name":"电视类型", type:str,"max_length":50, "min_length":0} \
        , "tv_score":{"_name":"电视评分", type:float, "max":10.00, "min":0.0} \
        , "tv_performer":{"_name":"演员", type:str, "max_length":100, "min_length":0} \
        , "tv_content":{"_name":"电视简介", type:str, "max_length":1024, "min_length":0} \
        , "tv_play_url":{"_name":"播放地址列表", type:dict}\
        , "tv_index":{"_name":"电视集数", type:int, "min":0, "max":1000}\
        , "tv_state":{"_name":"电视更新状态", type:str, "min_length":0, "max_length":100}\
        , "tv_area":{"_namme":"电视区域", type:str, "min_length":0, "max_length":100}\
        , "tv_language":{"_name":"电视语言", type:str, "min_length":0, "max_length":100}}

    __msg__ = {
        "type": "%s类型错误",
        "max_length": "%s长度太长",
        "min_length": "%s长度太短",
        "min": "% 数据太小",
        "max": "% 数据太大"
    }#和__invalid__ 数据错误对应

    error_msg = ""
