from django.urls import path
from accounts.views.signout import *

urlpatterns = [
	path('signout/',signout,name="signout"),
]