"""
WSGI config for cloud_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/mayank/PES/Sem6/CC/cloud/')
sys.path.append('/home/mayank/PES/Sem6/CC/selfie-less-act/')
sys.path.append('/home/mayank/PES/Sem6/CC/selfie-less-act/cloud_project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'cloud_project.settings'

application = get_wsgi_application()
