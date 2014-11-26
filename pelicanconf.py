#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site setings
AUTHOR = u'Javier V. Gómez'
SITENAME = u'JV - Science and stuff.'
SITEURL = 'https://jvgomez.github.io'
#AUTHOR_URL = ''
#SITEURL = ''
TIMEZONE = 'Europe/Madrid'

GOOGLE_ANALYTICS = 'UA-21664985-2'
DISQUS_SITENAME = 'jvgomez'

DEFAULT_LANG = u'en'
THEME = 'tuxlite_tbs'

# Pelican paths
PATH = 'content'
STATIC_PATHS = ['images', 'files']
PLUGIN_PATHS = ["pelican-plugins"]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Plugins activation
PLUGINS = ['extract_toc', 'liquid_tags.youtube', 'better_code_samples']
MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra', 'toc']

RESPONSIVE_IMAGES = True
LOAD_CONTENT_CACHE = False

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
