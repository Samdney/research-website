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
    ('Research', '/research.html'),
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

# Upcoming Stuff
#UPCOMING = ""

# Status Report
STATUS_REPORT = ('Medium', '#1: Getting ordered, collecting money', 'https://medium.com/@carolinzoebelein/status-report-1-getting-ordered-collecting-money-fe549b05bd59?source=friends_link&sk=21746e4733102fbbad9e8515bb39f66d', '2019/10/24', 'This article is the first one of a new series, a kind of newsletter, for updating you what have happened in the last weeks or months related to my work as independent mathematical research scientist and also a bit about my art work. ....')

# Article
ARTICLE = ('Medium', 'Independent mathematical scientist. wat?', 'https://medium.com/@carolinzoebelein/independent-mathematical-scientist-wat-9691639a6ced?source=friends_link&sk=10ffa3a64a1812b8ea360ce925df9e1a', '2019/10/03', 'Already for a longer time, I wanted to start with writing Medium articles. My thinking was always to start with any technical content, since writing about themselves, at first,would be too egocentric. But now, ....')

# Q&A
#QA = ('Misc', 'B', 'C', 'D', 'E')

# Work
WORK = " "
WORK_LINKS_EXTERNAL = (
    ('General docs', 'https://cryptpad.fr/profile/#/2/profile/view/ZGoqJnzLDklP5gYiOFE15ecC8dVMzFSiudqHeTE0Ms4/'),
    ('Schedule', 'https://cryptpad.fr/sheet/#/2/sheet/view/ym+olKCrTCwl2MTIOtaRrmzzNyXyh6e8HOCn1xIwKWw/'),
    ('GitHub', 'https://github.com/Samdney'),
    ('GitLab', 'https://gitlab.com/Samdney'),
    ('ResearchGate', 'https://www.researchgate.net/profile/Carolin_Zoebelein'),
    ('arXiv', 'https://arxiv.org/search/?searchtype=author&query=Z%C3%B6belein%2C+C')
)

WORK_LINKS = (
    ('Preprints', '/public.html#Preprints'),
    ('Notes', '/public.html#Notes'),
    ('Worksheets', '/public.html#Worksheets'),
    ('Meetups', '/public.html#Meetups')
)

# Combsee
COMBSEE = "<font style='color: grey;'>Decentralized search for more privacy.</font><br />A new type of decentralized, privacy preserving, search engine based on its mathematical design."
COMBSEE_LINK = 'https://www.combsee.org/'

# GitHub
GITHUB_USER = ('Samdney', 'https://github.com/Samdney')
GITHUB_LINKS = (
    ('Proposals', 'https://github.com/Samdney/proposals'),
    ('Papers', 'https://github.com/Samdney/papers'),
    ('Notes', 'https://github.com/Samdney/notes')
)

# Ongoing Events
#TALKS = ""
#MEETUPS = ""
#WEBINARS = ""
PROJECTS = "project_0055"
FUNDINGS = "funding_0003"
#CROWDFUNDING_CAMPAIGNS = "GoFundMe.com: <i>Conference Attending Expenses</i> (<a href='https://www.gofundme.com/f/conference-attending-expenses' title='GoFundMe.com: Conference Attending Expenses' target='_blank' style='color: #2196F3;'>visit</a>)"

# PGP Keys
SIGNING_KEY = u'8F31 C7C6 E67E 9ACE 8E12 E2EF 0DE3 A4D3 BA87 2A8B'

# Social
SOCIAL = (
    ('Twitter', 'fab', 'fa', 'twitter', 'https://twitter.com/SamdneyTweet','@SamdneyTweet<br /> Tweets and Work updates'),
    ('Blog', 'fas', 'fa', 'pencil-alt', 'https://Samdney.github.io', 'Mostly math'),
    ('Medium', 'fab', 'fa', 'medium', 'https://medium.com/@carolinzoebelein', 'Articles'),
    ('Reddit', 'fab', 'fa', 'reddit', 'https://www.reddit.com/user/CarolinZoebelein', 'Brainstorming forum questions and answers'),
    ('GitHub', 'fab', 'fa', 'github', 'https://github.com/Samdney', '@Samdney<br /> Code, Research Notes, Worksheets, Proposals and Papers'),
    ('GitLab', 'fab', 'fa', 'gitlab', 'https://gitlab.com/Samdney', '@Samdney<br /> Code, Art Projects, Notes'),
    ('Mathoverflow', 'ai', 'ai', 'mathoverflow', 'https://mathoverflow.net/users/147606/samdney?tab=profile', 'Mathematics Q&A'),
    ('ResearchGate', 'ai', 'ai', 'researchgate', 'https://www.researchgate.net/profile/Carolin_Zoebelein', 'Research overview'),
    ('arXiv', 'ai', 'ai', 'arxiv', 'https://arxiv.org/search/?searchtype=author&query=Z%C3%B6belein%2C+C', 'ePrints and Preprints'),
    ('General', 'fas', 'fa', 'globe', 'https://www.carolin-zoebelein.de', 'General website'),
    ('Art', 'far', 'fa', 'images', 'https://art.carolin-zoebelein.de', 'Website about my art work'),
)

SOCIAL_SIGNS = (
    ('Twitter', 'fab', 'fa', 'twitter'),
    ('Blog', 'fas', 'fa', 'pencil-alt'),
    ('Medium', 'fab', 'fa', 'medium'),
    ('GitHub', 'fab', 'fa', 'github'),
    ('GitLab', 'fab', 'fa', 'gitlab'),
    ('ResearchGate', 'ai', 'ai', 'researchgate'),
    ('arXiv', 'ai', 'ai', 'arxiv'),
    ('Website', 'fas', 'fa', 'globe'),
    ('General', 'fas', 'fa', 'globe'),
    ('Art', 'far', 'fa', 'images'),
    ('Misc', 'fas', 'fa', 'cat'),
)

SOCIAL_PAGINATION = 4

#DEFAULT_PAGINATION = 6
DEFAULT_PAGINATION = False
INDEX_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
