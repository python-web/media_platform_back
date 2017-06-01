#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime
from models.base_model import BaseModel
class Movie(BaseModel):
    __table__ = "movie"
    #play_url : 视频类型(mp4|m3u8) url 清晰度(高清)
    __invalid__ = {"movie_id":{"_name":"电影ID", type:str, "max_length":100, "min_length":0}\
        , "movie_name":{"_name":"电影名称", type:str, "max_length":50, "min_length":0}\
        , "movie_image_path":{"_name":"电影截图地址", type:str, "max_length":320, "min_length":0}\
        , "movie_born":{"_name":"电影上映日期", type:datetime}\
        , "movie_category":{"_name":"电影类型", type:str,"max_length":50, "min_length":0}\
        , "movie_score":{"_name":"电影评分", type:float, "max":10.00, "min":0.0}\
        , "movie_performer":{"_name":"演员", type:str, "max_length":100, "min_length":0}\
        , "movie_content":{"_name":"电影简介", type:str, "max_length":1024, "min_length":0}\
        , "movie_play_url":{"_name":"播放地址", type:list}\
        , "movie_state":{"_name":"视频状态", type:str, "max_length":1024, "min_length":0}\
        , "movie_area":{"_name":"电影区域", type:str, "max_length":1024, "min_length":0}\
        , "movie_language":{"_name":"电影语言", type:str, "max_length":1024, "min_length":0}}
    __msg__ = {
        "type": "%s类型错误",
        "max_length": "%s长度太长",
        "min_length": "%s长度太短",
        "min": "% 数据太小",
        "max": "% 数据太大"
    }#和__invalid__ 数据错误对应
    error_msg = ""
