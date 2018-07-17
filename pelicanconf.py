#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
from datetime import time
from datetime import datetime


AUTHOR = u'Carolin Zöbelein'
SITENAME = u'Carolin Zöbelein - Research'
SITEURL = ''

PATH = 'content'

# *** TODO ***
STATIC_PATHS = ['blog', 'pages', 'images']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'

PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

SUMMARY_MAX_LENGTH = None
# *** TODO ***


TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Theme
THEME = 'themes/MinimalXY'

# Theme customizations
MINIMALXY_START_YEAR = 2018
MINIMALXY_CURRENT_YEAR = date.today().year

# Menu      # TODO: '/categories.html'
MENUITEMS = (
    #('About', '/about.html'),
    #('Projects', '/projects.html'),
    ('Crowdfunding', '/crowdfunding.html'),
    ('Contact', '/contact.html'),
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = u'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

# PGP Keys
SIGNING_KEY = u'8F31 C7C6 E67E 9ACE 8E12 E2EF 0DE3 A4D3 BA87 2A8B'

# Social
SOCIAL = (
    ('Twitter', 'fa', 'twitter', 'http://twitter.com/SamdneyTweet'),
    ('Blog', 'fa', 'pencil', 'https://Samdney.github.io'),
    ('GitHub', 'fa', 'github', 'https://github.com/Samdney'),
    ('GitLab', 'fa', 'gitlab', 'http://gitlab.com/Samdney'),
    ('arXiv', 'ai', 'arxiv', 'https://arxiv.org/search/?searchtype=author&query=Z%C3%B6belein%2C+C'),

)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
