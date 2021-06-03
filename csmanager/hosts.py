from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
	host(r'', settings.ROOT_URLCONF, name='main'),
	host(r'(?P<company>\w+)', 'dashboard.urls', name="dashboard")
)