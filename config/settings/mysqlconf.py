
# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# DATABASES = {
#     # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
#     'default': env.db("DATABASE_URL", default="postgres:///zhiliao"),
# }
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zhiliao',
        'USER': 'ygs',
        'PASSWORD': '0000',
        'HOST': '',
        'PORT': '3306',
        # 'OPTIONS': {
        #     'read_default_file': '/etc/my.cnf',
        # },
    },
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
