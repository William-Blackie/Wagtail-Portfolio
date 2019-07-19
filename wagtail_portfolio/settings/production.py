from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('wagtail_blog_secret_key')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['63.32.111.162']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
try:
    from .local import *
except ImportError:
    pass
