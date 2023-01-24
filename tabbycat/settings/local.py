import dj_database_url

ON_LOCAL = True

# ==============================================================================
# Settings that you should specify
# ==============================================================================

if os.getenv("DATABASE_URL", None) is None:
    raise Exception("DATABASE_URL environment variable not defined")
DATABASES = {
    "default": dj_database_url.parse(os.getenv("DATABASE_URL")),
}

if not STATIC:
    SERVER_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
    DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = os.getenv('EMAIL_PORT')
    EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'False') != 'False'

# Replace this with your time zone, as defined in the IANA time zone database:
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
TIME_ZONE = 'Asia/Istanbul'

# ==============================================================================
# Overwrites main settings
# ==============================================================================

ADMINS              = ()
MANAGERS            = ADMINS
DEBUG               = os.getenv('DEBUG', 'False') == 'True'
DEBUG_ASSETS        = True
SECRET_KEY          = os.getenv('DJANGO_SECRET_KEY')
STATIC = os.getenv('DJANGO_STATIC', 'False') == 'True'
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"
# ==============================================================================
# Django-specific Modules
# ==============================================================================

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1'
)

# ==============================================================================
# Caching
# ==============================================================================

PUBLIC_FAST_CACHE_TIMEOUT   = 0
PUBLIC_SLOW_CACHE_TIMEOUT   = 0
TAB_PAGES_CACHE_TIMEOUT     = 0

CACHES = { # Use a dummy cache in development
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
   }
}

# Use the cache with database write through for local sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
