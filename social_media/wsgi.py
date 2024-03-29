"""
WSGI config for social_media project.

It exposes the WSGI callable as Practice_codes module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media.settings')

application = get_wsgi_application()
