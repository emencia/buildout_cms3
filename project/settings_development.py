"""
Settings to use for development
"""
from settings import *

# Enable django-debug-toolbar for the following IPs
INTERNAL_IPS = ('192.168.0.112',)

# Test emails by looking at the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# googletools is disabled when DEBUG=True, you can force to enable it with 
# uncommenting this line
#GOOGLETOOLS_ENABLED = True
