#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from handlers.base_handler import BaseHandler, RenderInfo
from io import StringIO
from utils.common_data import MovieInfoName
from models.movie_info import Movie
import json
import os.path
import csv
import tornado.web
import tornado.gen

class MovieHandler(BaseHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        if args and 0 < len(args):
            operation = args[0]
            if operation == "add":
                self.render("movie/movie_add.html")
            if operation == 'del':
                self.render("movie/movie_del.html")
            if operation == 'info':
                movies_info = yield self._show_info()
                # self.render("movie/movie_info_test.html", movie_count=len(movies_info), movie_info=movies_info)
                self.render("movie/movie_info.html", movie_count=len(movies_info), movie_info=movies_info)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        if args and 0 < len(args):
            operation = args[0]
            if operation == "add":
                result = yield self._add_movie()
                self.render("movie/movie_add.html")
            if operation == 'del':
                movie_id = self.get_argument(MovieInfoName.ID.value, None)
                movie_name = self.get_argument(MovieInfoName.Name.value, None)
                result = yield self._del_movie(movie_id=movie_id, movie_name=movie_name)
                self.render("movie/movie_del.html")
            if operation == "export":
                self._export_movies()
                self.write(json.dumps({'success':True}))
                #self.render("movie/movie_add.html")

    @tornado.gen.coroutine
    def _show_info(self, search_length=20):
        movie_cursor = self.db.movie.find()
        movie_lists = yield movie_cursor.to_list(length=search_length)
        movie_info_list = []
        for item in movie_lists:
            movie_render = RenderInfo(item)
            movie_info_list.append(movie_render)
        return movie_info_list

    @tornado.gen.coroutine
    def _add_movie(self):
        movie_name_list = [MovieInfoName.ID.value, MovieInfoName.Name.value \
            , MovieInfoName.Born.value, MovieInfoName.State.value \
            , MovieInfoName.Category.value, MovieInfoName.Score.value \
            , MovieInfoName.Performer.value, MovieInfoName.Content.value \
            , MovieInfoName.Area.value \
            , MovieInfoName.Language.value]

        movie_info = {item:self.get_argument(item, None) for item in movie_name_list }

        #处理图片
        image_name = self.request.files.get(MovieInfoName.ImagePath.value)
        for item in image_name:
            movie_image_path = 'images/movie/{0}'.format(item.filename)
            movie_info.update({MovieInfoName.ImagePath.value:movie_image_path})
            static_image_path = os.path.join(self.settings.get("static_path"), "movie", item.filename)
            with open(static_image_path, 'wb') as fd:
                fd.write(item.body)
        #处理播放地址
        url = self.get_argument(MovieInfoName.PlayUrl.value, None)
        video_type = self.get_argument("play_url_video_type", None)
        video_choice = self.get_argument("play_url_video_choice", None)
        play_list =  [[video_type, url,video_choice]]
        movie_info.update({MovieInfoName.PlayUrl.value:play_list})
        result = yield self.db.movie.insert(movie_info)
        return result

    @tornado.gen.coroutine
    def _del_movie(self, movie_id=None, movie_name=None):
        if movie_id:
            result = yield self.db.movie.delete_many({MovieInfoName.ID.value: movie_id})
            return result
        elif movie_name:
            result = yield self.db.movie.delete_many({MovieInfoName.Name.value:movie_name})
            return result
        else:
            pass

    @tornado.gen.coroutine
    def _export_movies(self):
        """
        通过CSV文件导入电影信息
        :return: 
        """
        if self.request.files and isinstance(self.request.files, dict) and "qqfile" in self.request.files:
            file_lists = self.request.files.get("qqfile")
            insert_result = False
            for item in file_lists:
                data = item.get("body")
                data_str = StringIO(data.decode('gb2312'))
                reader = csv.DictReader(data_str)
                movie_info_list = []
                for row in reader:
                    movie_template_name_map = {"电影名称":MovieInfoName.Name.value\
                                                  , "电影ID":MovieInfoName.ID.value\
                                                  , "电影上映日期":MovieInfoName.Born.value\
                                                  , "电影类型":MovieInfoName.Category.value\
                                                  , "电影评分":MovieInfoName.Score.value\
                                                  , "电影演员":MovieInfoName.Performer.value\
                                                  , "电影状态":MovieInfoName.State.value\
                                                  , "电影区域":MovieInfoName.Area.value\
                                                  , "电影语言":MovieInfoName.Language.value\
                                                  , "电影简介":MovieInfoName.Content.value\
                        , "电影图片地址":MovieInfoName.ImagePath.value\
                        , "电影播放地址":MovieInfoName.PlayUrl.value}
                    movie_info = {}
                    for key, value in row.items():
                        movie_info[movie_template_name_map.get(key)] = value
                    #处理图片
                    url = movie_info.get(MovieInfoName.PlayUrl.value, None)
                    play_list =  []
                    for item in  url.split(";"):
                        play_items = item.split(",")
                        if play_items and 3 <= len(play_items):
                            video_type = play_items[0]
                            url = play_items[1]
                            video_choice = play_items[2]
                            play_list.append([video_type, url, video_choice])
                    movie_info.update({MovieInfoName.PlayUrl.value:play_list})
                    movie_info_list.append(movie_info)
                result = yield self.db.movie.insert_many(movie_info_list)
                if result:
                    insert_result = True
            return insert_result
        else:
            return False

    def check_xsrf_cookie(self):
        pass
