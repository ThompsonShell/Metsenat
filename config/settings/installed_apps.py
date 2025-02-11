DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MY_PROJECT_APPS = [
    'apps.appeals',
    'apps.users',
    'apps.sponsors',
    'apps.general',
    'apps.utils',
    'apps.authentication'

]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'drf_yasg'


]

INSTALLED_APPS = DJANGO_APPS + MY_PROJECT_APPS +THIRD_PARTY_APPS