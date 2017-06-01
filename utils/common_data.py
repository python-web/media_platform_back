#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from enum import IntEnum

from enum import Enum


class MediaType(Enum):
    TV = 0
    Movie = 1
    Cartoon = 2
    M3D = 3

class MediaTypeName(Enum):
    TVName = "tv"
    MovieName = "movie"
    CartoonName = "cartoon"
    M3D = "3d"
class UserType(IntEnum):
    Admin = 0
    User = 1
    Guest = 2

UserInfoName = "user_info"
CurrentUserName = "current_user"

class UserInfoTableName(Enum):
    ID = "_id"
    UserName="name"
    Password = "password"
    Power="power"
    LoginTime="time"

class MovieInfoName(Enum):
    ID = "movie_id"
    Name = "movie_name"
    ImagePath = "movie_image_path"
    Born = "movie_born"
    Category = "movie_category"
    Score = "movie_score"
    Performer = "movie_performer"
    Content = "movie_content"
    PlayUrl = "movie_play_url"
    Area = "movie_area"
    Language = "movie_language"
    State = "movie_state"


class TVInfoName(Enum):
    ID = "tv_id"
    Name = "tv_name"
    ImagePath = "tv_image_path"
    Born = "tv_born"
    Category = "tv_category"
    Score = "tv_score"
    Performer = "tv_performer"
    Content = "tv_content"
    PlayUrl = "tv_play_url"
    Index = "tv_index"
    State = "tv_state"
    Area = "tv_area"
    Language = "tv_language"

class MovieInfo():
    def __init__(self, id, categeroy=None\
                 , name=None\
                 , score=None\
                 , performer=None\
                 , born=None\
                 , image_path=None):
        self._movie_id = id
        self._born = born
        self._categeroy = categeroy
        self._movie_name = name
        self._score = score
        self._performer = performer
        self._image_path = image_path
        self._play_url = None

    @property
    def play_url(self):
        return "/play/{0}".format(self._movie_id)

    @property
    def image_path(self):
        return self._image_path

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def born(self):
        return self._born

    @property
    def categeroy(self):
        return self._categeroy

    @property
    def movie_name(self):
        return self._movie_name

    @property
    def score(self):
        return self._score

    @property
    def performer(self):
        return self._performer
