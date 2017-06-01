#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import os.path
etc = {}
etc['error'] = False
etc['template_path'] = os.path.join('views')
etc['static_path'] = os.path.join(os.path.dirname(__file__), 'static')
etc['cookie_secret'] = "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E="
etc['session_secret'] = "3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc"
etc['session_timeout'] = 60
etc['xsrf_cookies'] = True
etc['debug'] = True
etc['login_url'] = "/login"
