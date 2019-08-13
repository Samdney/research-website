#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
from datetime import time
from datetime import datetime


AUTHOR = u'Carolin Zöbelein'
AUTHOR_AVATAR = u'/images/zoebelein_avatar.png'
SITENAME = u'Carolin Zöbelein - Research'
SITEURL = ''
SITEURL_SOCIAL = 'https://research.carolin-zoebelein.de'
KEYWORDS = ('Carolin Zöbelein', 'Research', 'Mathematical', 'Scientist',
        'Freelancer', 'Math', 'Crytography', 'Algebra', 'Number Theory', 'Funding',
        'Crowdfunding', 'Encryption', 'Privacy', 'Anonymity', 'Communication',
        'Free', 'Access', 'Independently', 'Obfuscation', 'Anti-Censorship',
        'Censorship', 'Blocking', 'Circumvention', 'Protecting',
        'Decentralized', 'Networks', 'Technologies', 'Search Engine',
        'Protocol', 'Prime numbers', 'Android', 'App', 'Security', 'Art')

PATH = 'content'
# ******
# Plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['jinja2content']
# ******
STATIC_PATHS = ['blog', 'pages', 'images', 'files', 'qrcodes']
ARTICLE_PATHS = ['blog']
#ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
#ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{slug_dir}/{slug_subdir}/{slug}.html'
ARTICLE_URL = '{slug_dir}/{slug_subdir}/{slug}.html'

PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

SUMMARY_MAX_LENGTH = None
# ******


TIMEZONE = 'Europe/Paris'

DATE_FORMATS = {
        'en': '%Y/%m/%d',
}

DEFAULT_LANG = u'en'

# Theme
THEME = 'themes/MinimalXY'

# Theme customizations
MINIMALXY_START_YEAR = 2018
MINIMALXY_CURRENT_YEAR = date.today().year

# Icon
MINIMALXY_FAVICON = 'images/favicon.ico'

# Menu
MENUITEMS = (
    ('About', '/about.html'),
    ('Projects', '/projects.html'),
    ('Public', '/public.html'),
    ('Funding', '/funding.html'),
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

# Index introduction
INDEX_INTRO_IMAGE = '/images/john-moeses-bauan-690280-unsplash.jpg'
INDEX_INTRO_TITLE = 'Welcome'
INDEX_INTRO_CONTENT = 'Research. Free and Independently.'

# Ongoing Events
#TALKS = ""
#MEETUPS = ""
#WEBINARS = ""
#PROJECTS = ""
#FUNDINGS = ""
CROWDFUNDING_CAMPAIGNS = "GoFundMe.com: <i>Conference Attending Expenses</i> (<a href='https://www.gofundme.com/f/conference-attending-expenses' title='GoFundMe.com: Conference Attending Expenses' target='_blank' style='color: #2196F3;'>visit</a>)"
SCHEDULE = "My public <a href='/about.html#Schedule' title='Schedule' style='color: #2196F3;'>schedule</a> for my projects and fundings."

# PGP Keys
SIGNING_KEY = u'8F31 C7C6 E67E 9ACE 8E12 E2EF 0DE3 A4D3 BA87 2A8B'

# Social
SOCIAL = (
    ('Twitter', 'fab', 'fa', 'twitter', 'https://twitter.com/SamdneyTweet'),
    ('Blog', 'fas', 'fa', 'pencil-alt', 'https://Samdney.github.io'),
    ('Medium', 'fab', 'fa', 'medium', 'https://medium.com/@carolinzoebelein'),
    ('General', 'fas', 'fa', 'globe', 'https://www.carolin-zoebelein.de'),
    ('Art', 'far', 'fa', 'images', 'https://art.carolin-zoebelein.de'),
    ('GitHub', 'fab', 'fa', 'github', 'https://github.com/Samdney'),
    ('GitLab', 'fab', 'fa', 'gitlab', 'https://gitlab.com/Samdney'),
    ('arXiv', 'ai', 'ai', 'arxiv', 'https://arxiv.org/search/?searchtype=author&query=Z%C3%B6belein%2C+C'),
)

SOCIAL_SIGNS = (
    ('Twitter', 'fab', 'fa', 'twitter'),
    ('Blog', 'fas', 'fa', 'pencil-alt'),
    ('Medium', 'fab', 'fa', 'medium'),
    ('General', 'fas', 'fa', 'globe'),
    ('Art', 'far', 'fa', 'images'),
    ('GitHub', 'fab', 'fa', 'github'),
    ('GitLab', 'fab', 'fa', 'gitlab'),
    ('arXiv', 'ai', 'ai', 'arxiv'),
    ('Website', 'fas', 'fa', 'globe'),
    ('Misc', 'fas', 'fa', 'cat'),
)

SOCIAL_PAGINATION = 4

#DEFAULT_PAGINATION = 6
DEFAULT_PAGINATION = False
INDEX_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
