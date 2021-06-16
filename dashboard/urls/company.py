from django.urls import path
from dashboard.views.company import company

urlpatterns = [
    path('<str:company>/', company, name="company"),
]