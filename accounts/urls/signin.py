from django.urls import path
from accounts.views.signin import *

urlpatterns = [
	path('signin/',signin.as_view(),name="signin"),
]