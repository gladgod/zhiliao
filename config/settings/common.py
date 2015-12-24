# -*- coding: utf-8 -*-
"""
Django settings for zhiliao project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from __future__ import absolute_import, unicode_literals

import environ

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
APPS_DIR = ROOT_DIR.path('zhiliao')

env = environ.Env()


# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Admin
    'django.contrib.admin',
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

)
THIRD_PARTY_APPS = (
    'crispy_forms',  # Form layouts
    'django_comments',
    # "django_extensions",
    # "compressor",
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'zhiliao.users',  # custom users app

    # Your stuff: custom apps go here

    "zhiliao.boot",
    "zhiliao.conf",

    "zhiliao.core",

    "zhiliao.generic",

    "zhiliao.pages",
    "zhiliao.blog",
    "zhiliao.forms",
    "zhiliao.galleries",
    # "zhiliao.twitter",
    "zhiliao.accounts",
    # "zhiliao.mobile",


    "zhiliao.grappellisafe",
    "zhiliao.filebrowsersafe",
)
#
PACKAGE_NAME_FILEBROWSER = "zhiliao.filebrowsersafe"
PACKAGE_NAME_GRAPPELLI = "zhiliao.grappellisafe"


# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'zhiliao.core.middleware.UpdateCacheMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "zhiliao.core.request.CurrentRequestMiddleware",
    "zhiliao.core.middleware.RedirectFallbackMiddleware",
    "zhiliao.core.middleware.TemplateForDeviceMiddleware",
    "zhiliao.core.middleware.TemplateForHostMiddleware",
    "zhiliao.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "zhiliao.core.middleware.SitePermissionMiddleware",
    # Uncomment the following if using any of the SSL settings:
    # "zhiliao.core.middleware.SSLRedirectMiddleware",
    "zhiliao.pages.middleware.PageMiddleware",
    "zhiliao.core.middleware.FetchFromCacheMiddleware",
)

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.

# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {
    'sites': 'zhiliao.contrib.sites.migrations'
}

# DEBUG = env.bool('DJANGO_DEBUG', default=True)

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("""gladgod""", 'gladgod@aliyun.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS



# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code

LANGUAGE_CODE = 'zh-hans'
# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(ROOT_DIR.path('templates')),
            # '/home/ygs/PycharmProjects/zhiliao/zhiliao/pages/templates',
            # '/home/ygs/PycharmProjects/zhiliao/zhiliao/core/templates',
            # '/home/ygs/PycharmProjects/zhiliao/zhiliao/generic/templates',
            # str(ROOT_DIR.path('templates')),
        ],
        # 'APP_DIRS': True,
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': True,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',

                'django.template.context_processors.i18n',
                'django.template.context_processors.media',

                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',

                # Your stuff: custom template context processors go here
                "zhiliao.conf.context_processors.settings",
                "zhiliao.pages.context_processors.page",
            ],
        },
    },
]

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(ROOT_DIR('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    # 'django.contrib.auth.backends.ModelBackend',
# 'allauth.account.auth_backends.AuthenticationBackend',
    'zhiliao.core.auth_backends.MezzanineBackend',
)

# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_URL = 'account_login'

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

########## CELERY
# INSTALLED_APPS += ('zhiliao.taskapp.celery.CeleryConfig',)
# # if you are not using the django database broker (e.g. rabbitmq, redis, memcached), you can remove the next line.
# INSTALLED_APPS += ('kombu.transport.django',)
# BROKER_URL = env("CELERY_BROKER_URL", default='django://')
########## END CELERY


# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r'^admin/'

# Your common stuff: Below this line define 3rd party library settings



# If True, the django-modeltranslation will be added to the
# INSTALLED_APPS setting.
USE_MODELTRANSLATION = False


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

FILE_UPLOAD_PERMISSIONS = 0664