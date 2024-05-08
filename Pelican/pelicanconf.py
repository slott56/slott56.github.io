AUTHOR = 'S.Lott'
SITENAME = 'S.Lott -- Software Architect'
SITEURL = ''
MASTODON_CLAIM = 'https://fosstodon.org/@slott56'

PATH = 'content'

STATIC_PATHS = [
  'media',
]

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_DOMAIN = SITEURL
FEED_ALL_RSS = "feeds/all.rss.xml"
FEED_RSS = "feeds/rss.xml"

# Blogroll
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/'),
    ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
)

# Social widget
SOCIAL = (
    ('Mastodon', 'https://fosstodon.org/@slott56'),
    ('Github', 'https://github.com/slott56'),
    ('StackOverflow', 'https://stackoverflow.com/users/10661/s-lott'),
    ('LinkedIn', 'https://www.linkedin.com/in/steven-lott-029835/'),
    # Packt
    ("O'Reilly", 'https://www.oreilly.com/pub/au/6277'),
    ("Amazon", 'https://www.amazon.com/stores/Steven-Lott/author/B00HNRSLEK'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "/Users/slott/Documents/Writing/Blogs/pelican-themes/pelican-bootstrap3"

PLUGIN_PATHS = ['/Users/slott/Documents/Writing/Blogs/pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

BANNER_SUBTITLE = "Rants on the daily grind of building software."
USE_FOLDER_AS_CATEGORY = False
ARTICLE_ORDER_BY = 'reversed-date'
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_ARCHIVE_ON_SIDEBAR = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
DOCUTIL_CSS = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
