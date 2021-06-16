from django.urls import path
from django.urls.resolvers import URLPattern
from dashbaord.views.ivr import *

urlpatterns = [
    path('answer/<str:companyName>/', answerCompanyPhone, name="answerCompanyPhone"),
]