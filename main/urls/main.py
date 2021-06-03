from django.urls import path
from main.views.main import main

urlpatterns = [
	path("", main, name="main"),
]