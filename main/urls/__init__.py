from django.urls import path, include
# from main.views.__init__ import VIEW_NAME
from . import main as mainUrls

urlpatterns = [
	path("", include(mainUrls))	
]