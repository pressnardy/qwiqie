"""
WSGI config for qwiqie project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ.get('DJANGO_ENV') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qwiqie.production_settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qwiqie.settings')

application = get_wsgi_application()
