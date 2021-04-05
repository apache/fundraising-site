#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = u'Fundraising'
SITENAME = u'Apache Fundraising'
SITEURL = ''
CURRENTYEAR = date.today().year

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'
SITEURL = '.'
RELATIVE_URLS = False
PAGE_SAVE_AS = './{slug}.html'
ARTICLE_SAVE_AS = 'news/{slug}.html'
ARTICLE_URL = 'news/{slug}.html'

# Sort news by date, descending, latest article first
ARTICLE_ORDER_BY = 'reversed-date'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# TOC Generator
PLUGIN_PATHS = ['./theme/plugins']
PLUGINS = ['toc']
TOC_HEADERS = r"h[1-6]"

# Blogroll
LINKS = (('The Apache Software Foundation', 'https://www.apache.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
