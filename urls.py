#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from handlers.api_home_handler import ApiHomeHandler
from handlers.movie_handler import MovieHandler
from handlers.tv_handler import TVHandler
from handlers.login_handler import LoginHandler
urls = [(r"/", ApiHomeHandler),
        (r"/login", LoginHandler),
        (r"/api/movie/(.*)", MovieHandler),
        (r"/api/tv/(.*)", TVHandler)]
