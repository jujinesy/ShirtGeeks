"""
Django settings for ShirtGeeks project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import json

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

secret_file = os.path.join(os.path.dirname(BASE_DIR)+"/runfile", 'secret.json')

with open(secret_file, 'r') as f:
    secret = json.loads(f.read())

def get_secret(setting, secret=secret):
    """
    :param setting: secret Dict 의 원하는 value 값을 가져올 수 있게하는 key 값
    :param secret: 비밀 변수들의 실제 값을 담은 json 파일을 Dict화 한 변수
    :return secret[setting]: secret.json 에서 가져온 Dict 의 setting 키를 가진 값을 리턴해줍니다.
    """
    try:
        return secret[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

LOCAL = False
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'j2b_z(*4w+#)t^nz3)0n3da(tcj&3##klo73m76(x7%3z)b%85n!')
SECRET_KEY = get_secret('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
try:
    from .local import *
except:
    DEBUG = False
    pass
print('DEBUG : {}'.format(DEBUG))

SITE_ID = 1

ALLOWED_HOSTS = []

AUTO_CONFIRM = False

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = get_secret("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
DEFAULT_TO_EMAIL = EMAIL_HOST_USER

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'aaaa@gmail.com'
# EMAIL_HOST_PASSWORD = 'aaaa'
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# DEFAULT_TO_EMAIL = EMAIL_HOST_USER

ADMINS = (
    ('Admin', EMAIL_HOST_USER),
)
MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = [
    # External apps that need to go before django's
    # 'storages',

    # Django modules
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'django.contrib.postgres',
    'django.forms',

    # Local apps
    # 'saleor.account',
    # 'saleor.discount',
    # 'saleor.product',
    # 'saleor.cart',
    # 'saleor.checkout',
    'conf.core',
    # 'saleor.graphql',
    # 'saleor.menu',
    # 'saleor.order.OrderAppConfig',
    # 'saleor.dashboard',
    # 'saleor.seo',
    # 'saleor.shipping',
    # 'saleor.search',
    'conf.site',
    # 'saleor.data_feeds',
    # 'saleor.page',

    # External apps
    # 'versatileimagefield',
    'django_babel',
    # 'bootstrap4',
    # 'django_prices',
    'django_prices_openexchangerates',
    # 'graphene_django',
    # 'mptt',
    # 'payments',
    'webpack_loader',
    # 'social_django',
    'django_countries',
    # 'django_filters',
    # 'django_celery_results',
    # 'impersonate',
    # 'phonenumber_field'


    'django.contrib.admin',

    'menus',
    'profiles',
    'restaurants',
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'assets/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-bundle.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': [
            r'.+\.hot-update\.js',
            r'.+\.map']}}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.middleware.locale.LocaleMiddleware',
    'django_babel.middleware.LocaleMiddleware',
]

ROOT_URLCONF = 'conf.urls'
LOGIN_URL = '/login/'

context_processors = [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',

    'django.template.context_processors.i18n',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
    'django.template.context_processors.tz',
    # 'saleor.core.context_processors.default_currency',
    # 'saleor.cart.context_processors.cart_counter',
    # 'saleor.core.context_processors.navigation',
    # 'saleor.core.context_processors.search_enabled',
    'conf.site.context_processors.site',
    # 'social_django.context_processors.backends',
    # 'social_django.context_processors.login_redirect',
]

loaders = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader']

if not DEBUG:
    loaders = [('django.template.loaders.cached.Loader', loaders)]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': context_processors,
            # 'loaders': loaders,
            'libraries': {
                'custom_tags': 'templatetags.custom_tags',
            }
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '../..'))

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('bg', _('Bulgarian')),
    ('de', _('German')),
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fa-ir', _('Persian (Iran)')),
    ('fr', _('French')),
    ('hu', _('Hungarian')),
    ('it', _('Italian')),
    ('ja', _('Japanese')),
    ('ko', _('Korean')),
    ('nb', _('Norwegian')),
    ('nl', _('Dutch')),
    ('pl', _('Polish')),
    ('pt-br', _('Portuguese (Brazil)')),
    ('ro', _('Romanian')),
    ('ru', _('Russian')),
    ('sk', _('Slovak')),
    ('tr', _('Turkish')),
    ('uk', _('Ukrainian')),
    ('vi', _('Vietnamese')),
    ('zh-hans', _('Chinese'))]
LOCALE_PATHS = [os.path.join(PROJECT_ROOT, 'locale')]
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'   #주소창에보이는 스태틱주소
STATICFILES_DIRS = [
    os.path.join(BASE_DIR+"/Static/", "Static_Local"),
    #'/var/www/static/',
]
STATIC_ROOT = os.path.join(BASE_DIR+"/Static/", 'Static_Server')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR+"/Media/", 'Media_Server')

LOGOUT_REDIRECT_URL = '/login'
LOGIN_REDIRECT_URL = '/'

CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False



DEFAULT_COUNTRY = 'US'
DEFAULT_CURRENCY = 'USD'
AVAILABLE_CURRENCIES = [DEFAULT_CURRENCY]

ENABLE_SSL = False

ENABLE_SEARCH = False
