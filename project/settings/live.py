from project.settings.common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Make this unique, and don't share it with anybody.
import os
#SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY = "as@3oi2rF@#jf32l32l*fd"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'jaywhiletwo',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/tmp.log',
        },
    },
    'loggers': {
        '': {
            'handlers': ['mail_admins', 'log_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins', 'log_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

STATICFILES_DIRS = ()
STATIC_ROOT = '%s/assets/' % BASE_DIR
STATIC_URL = '/stc/'
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

LOCAL_RESOURCE = '/home/jlee/Backup/Pictures/'
