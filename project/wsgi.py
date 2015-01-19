"""
WSGI config for jaywhiletwo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.common")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
_application = DjangoWhiteNoise(get_wsgi_application())

env_variables_to_pass = ['SECRET_KEY', ]
def application(environ, start_response):
    # pass the WSGI environment variables on through to os.environ
    for var in env_variables_to_pass:
        os.environ[var] = environ.get(var, '')
    return _application(environ, start_response)
