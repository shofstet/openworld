import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for openworld project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.translation import ugettext_lazy as _
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rl=y-d-6tn($0=3k4bn8u0)6*14gggp!@&%c2p)(^wf22ez&wx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition





ROOT_URLCONF = 'openworld.urls'

WSGI_APPLICATION = 'openworld.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

TIME_ZONE = 'Europe/Zurich'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
os.path.join(BASE_DIR, 'openworld', 'static'),
)
SITE_ID = 1

TEMPLATE_LOADERS = (
'django.template.loaders.filesystem.Loader',
'django.template.loaders.app_directories.Loader',
'django.template.loaders.eggs.Loader'
)

MIDDLEWARE_CLASSES = (
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.locale.LocaleMiddleware',
'django.middleware.doc.XViewMiddleware',
'django.middleware.common.CommonMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',
'cms.middleware.user.CurrentUserMiddleware',
'cms.middleware.page.CurrentPageMiddleware',
'cms.middleware.toolbar.ToolbarMiddleware',
'cms.middleware.language.LanguageCookieMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages',
'django.core.context_processors.i18n',
'django.core.context_processors.debug',
'django.core.context_processors.request',
'django.core.context_processors.media',
'django.core.context_processors.csrf',
'django.core.context_processors.tz',
'sekizai.context_processors.sekizai',
'django.core.context_processors.static',
'cms.context_processors.cms_settings'
)

TEMPLATE_DIRS = (
os.path.join(BASE_DIR, 'openworld', 'templates'),
)

INSTALLED_APPS = (
'djangocms_admin_style',
'djangocms_text_ckeditor',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.admin',
'django.contrib.sites',
'django.contrib.sitemaps',
'django.contrib.staticfiles',
'django.contrib.messages',
'cms',
'menus',
'sekizai',
'treebeard',
'djangocms_style',
'djangocms_column',
'djangocms_file',
'djangocms_flash',
'djangocms_googlemap',
'djangocms_inherit',
'djangocms_link',
'djangocms_picture',
'djangocms_teaser',
'djangocms_video',
'reversion',
'openworld'
)

LANGUAGES = (
## Customize this
('de', gettext('German')),
('en', gettext('English')),
)

LANGUAGE_CODE = 'de'

CMS_LANGUAGES = {
## Customize this
1:[
    {
            'code': 'de',
            'name': gettext('Deutsch'),
            'fallbacks': ['en'],
            'public': True,
            'hide_untranslated': True,
            'redirect_on_fallback':False,
        },
        {
            'code': 'en',
            'name': gettext('English'),
            'fallbacks': ['de'],
            'public': True,
        },
    ],
    'default': {
        'fallbacks': ['de', 'en', ],
        'redirect_on_fallback': True,
        'hide_untranslated': False,
        'public': True,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('page.html', 'Page'),
    ('feature.html', 'Page with Feature')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
#         'content': {
#        'plugins': ['TextPlugin', 'PicturePlugin'],
#        'text_only_plugins': ['LinkPlugin'],
#        'extra_context': {"width":640},
#        'name': gettext("Content"),
#        'language_fallback': True,
#        'default_plugins': [
#            {
#                'plugin_type': 'TextPlugin',
#                'values': {
#                    'body':'<p>Lorem ipsum dolor sit amet...</p>',
#                },
#            },
#        ],
#        'child_classes': {
#            'TextPlugin': ['PicturePlugin', 'LinkPlugin'],
#        },
#        'parent_classes': {
#            'LinkPlugin': ['TextPlugin'],
#        },
#    },
    }

DATABASES = {
    'default':
        {'PASSWORD': 'silv.13', 'PORT': 5432, 'USER': 'shofstet', 'ENGINE': 'django.db.backends.postgresql_psycopg2', 'NAME': 'openworld', 'HOST': 'localhost'}
}

MIGRATION_MODULES = {
    'djangocms_column': 'djangocms_column.migrations_django',
    'djangocms_flash': 'djangocms_flash.migrations_django',
    'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    'djangocms_inherit': 'djangocms_inherit.migrations_django',
    'djangocms_link': 'djangocms_link.migrations_django',
    'djangocms_style': 'djangocms_style.migrations_django',
    'djangocms_file': 'djangocms_file.migrations_django',
    'djangocms_picture': 'djangocms_picture.migrations_django',
    'djangocms_teaser': 'djangocms_teaser.migrations_django',
    'djangocms_video': 'djangocms_video.migrations_django'
}
