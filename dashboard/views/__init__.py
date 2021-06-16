from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpRequest, HttpResponse
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.voice_response import VoiceResponse
from accounts.models import Company
from dashboard.models import Answer, Branch, Choice