from django.urls import path
from accounts.views.verify import *

urlpatterns = [
	path('verify/',verify.as_view(),name="verify"),
]