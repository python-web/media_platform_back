#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from handlers.base_handler import BaseHandler, RenderInfo
from utils.common_data import TVInfoName
from models.tv_info import TV
import os.path
import tornado.web
import tornado.gen

class TVHandler(BaseHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        if args and 0 < len(args):
            operation = args[0]
            if operation == "add":
                self.render("tv/tv_add.html")
            if operation == 'del':
                self.render("tv/tv_del.html")
            if operation == 'info':
                movies_info = yield self._show_info()
                # self.render("movie/movie_info_test.html", movie_count=len(movies_info), movie_info=movies_info)
                self.render("tv/tv_info.html", movie_count=len(movies_info), movie_info=movies_info)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        if args and 0 < len(args):
            operation = args[0]
            if operation == "add":
                result = yield self._add_movie()
                self.render("movie/movie_add.html")
            if operation == 'del':
                tv_id = self.get_argument(TVInfoName.ID.value, None)
                tv_name = self.get_argument(TVInfoName.Name.value, None)
                result = yield self._del_movie(movie_id=tv_id, movie_name=tv_name)
                self.render("movie/movie_del.html")

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
        movie_name_list = [TVInfoName.ID.value, TVInfoName.Name.value \
            , TVInfoName.Born.value, TVInfoName.State.value \
            , TVInfoName.Category.value, TVInfoName.Score.value \
            , TVInfoName.Performer.value, TVInfoName.Content.value \
            , TVInfoName.Area.value \
            , TVInfoName.Language.value]

        movie_info = {item:self.get_argument(item, None) for item in movie_name_list }

        #处理图片
        image_name = self.request.files.get(TVInfoName.ImagePath.value)
        for item in image_name:
            movie_image_path = 'images/movie/{0}'.format(item.filename)
            movie_info.update({TVInfoName.ImagePath.value:movie_image_path})
            static_image_path = os.path.join(self.settings.get("static_path"), "movie", item.filename)
            with open(static_image_path, 'wb') as fd:
                fd.write(item.body)
        #处理播放地址
        url = self.get_argument(TVInfoName.PlayUrl.value, None)
        video_type = self.get_argument("play_url_video_type", None)
        video_choice = self.get_argument("play_url_video_choice", None)
        play_list =  [[video_type, url,video_choice]]
        movie_info.update({TVInfoName.PlayUrl.value:play_list})
        result = yield self.db.movie.insert(movie_info)
        return result

    @tornado.gen.coroutine
    def _del_movie(self, movie_id=None, movie_name=None):
        if movie_id:
            result = yield self.db.movie.delete_many({TVInfoName.ID.value: movie_id})
            return result
        elif movie_name:
            result = yield self.db.movie.delete_many({TVInfoName.Name.value:movie_name})
            return result
        else:
            pass

    def check_xsrf_cookie(self):
        pass