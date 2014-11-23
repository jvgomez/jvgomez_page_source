#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Javier V. Gómez'
SITENAME = u'JV - Science and stuff.'
SITEURL = 'https://jvgomez.github.io/'
#SITEURL = ''
THEME = 'tuxlite_tbs'

PATH = 'content'
#STATIC_PATHS = ['blog']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('', 'http://stackoverflow.com/users/2283531/javi-v'),
          ('', 'http://github.com/jvgomez'),
          ('', 'https://www.linkedin.com/profile/view?id=105141580'),
         )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
