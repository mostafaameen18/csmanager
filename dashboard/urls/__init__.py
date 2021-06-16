from django.urls import path, include
# from dashboard.views.__init__ import VIEW_NAME
from . import company as company_urls
from . import ivr as ivr_urls

urlpatterns = [
	path('', include(company_urls)),
	path('', include(ivr_urls)),
]