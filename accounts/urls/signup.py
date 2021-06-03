from django.urls import path
from accounts.views.signup import *

urlpatterns = [
	path('signup/',signup.as_view(),name="signup"),
	path('checkSubdomain/', checkSubdomain, name="checkSubdomain"),
]