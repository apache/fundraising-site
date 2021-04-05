#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = u'Apache Fundraising'
SITENAME = u'Apache Fundraising'
CURRENTYEAR = date.today().year

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'
SITEURL = 'https://fundraising.apache.org/'
# Save pages using full directory preservation
PATH_METADATA= '.*?(pages/)?(?P<path_no_ext>.*?)\.[a-z]*$'
PAGE_SAVE_AS= './{slug}.html'
PAGE_URL= './{slug}.html'

ARTICLE_SAVE_AS = 'news/{slug}.html'
ARTICLE_URL = 'news/{slug}.html'

# TOC Generator
PLUGIN_PATHS = ['./theme/plugins']
PLUGINS = ['toc', 'pelican-gfm']
TOC_HEADERS = r"h[1-6]"

# Sort news by date, descending, latest article first
ARTICLE_ORDER_BY = 'reversed-date'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('The Apache Software Foundation', 'https://www.apache.org'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
