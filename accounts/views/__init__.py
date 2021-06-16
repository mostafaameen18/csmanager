from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django_hosts.resolvers import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client
from accounts.models import *
import string, json
from random import *



def codeGenerator():
	chars = string.ascii_letters + string.digits
	length = 8
	code = "".join(choice(chars) for i in range(length))

	is_repeated = False

	if Company.objects.filter(code=code).exists():
		return codeGenerator()
	else:
		return code


def subdomainModifier(subdomain):
	chars = string.digits
	length = 1
	code = "".join(choice(chars) for i in range(length))
	newSubdomain = subdomain + code

	if Company.objects.filter(subdomain=newSubdomain).exists():
		return subdomainModifier(subdomain)
	else:
		return newSubdomain