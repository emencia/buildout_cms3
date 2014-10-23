"""
Settings to use for development
"""
from settings import *

# Enable django-debug-toolbar for the following IPs
INTERNAL_IPS = ('192.168.0.112',)

# Test emails by looking at the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Enable raising exception from django-filer
FILER_DEBUG = True
