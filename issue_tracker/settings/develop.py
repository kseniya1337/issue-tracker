from .base import *

DEBUG = True


STATIC_URL = '/static/'

STATIC_ROOT = str(BASE_DIR.parent / 'public' / 'static')


MEDIA_URL = '/media/'

MEDIA_ROOT = str(BASE_DIR.parent / 'public' / 'media')
