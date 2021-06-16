from .__init__ import *

class signup(View):

	def get(self, request):

		if request.user.is_authenticated:
			return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

		available_countries = []
		client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
		available_phone_numbers = client.available_phone_numbers.list()
		for available_phone_number in available_phone_numbers:
			if available_phone_number.country_code == 'IL':
				continue
			available_countries.append(available_phone_number.country_code + " - " + available_phone_number.country)

		context = {
			"available_countries": sorted(available_countries),
		}

		if "OSN_SIGNUP_ERROR" in request.COOKIES:
			err = request.COOKIES['OSN_SIGNUP_ERROR']
			context['err'] = err

		res = render(request, "signup.html", context)
		res.delete_cookie('OSN_SIGNUP_ERROR')
		return res

	def post(self, request):

		if request.user.is_authenticated:
			return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		cname = request.POST.get('cname')
		phoneNumberCountry = request.POST.get('phoneNumberCountry').split(' - ')[0]
		subdomain = request.POST.get('subdomain')
		email = request.POST.get('email')
		password = request.POST.get('password')
		repass = request.POST.get('repass')
		image = request.FILES.get('image')

		if password == repass:

			try:
				user = User.objects.create_user(username=email, email=email, password=password, is_active=False)
				user.first_name = fname
				user.last_name = lname
				user.save()

				code = codeGenerator()

				# TODO: Get Twilio phone mumber and save it in next company instance
				
				company = Company(user=user, name=cname, subdomain=subdomain, code=code)
				if image:
					company.image = image
				company.save()

				subject = 'Submitted PO'
				message = ''
				context = {
					"code": code,
					"email": email,
				}
				msg_html = render_to_string('mail/verificationEmail.html', context)
				from_email = settings.EMAIL_HOST_USER
				to_list = [email]
				send_mail(subject, message, from_email, to_list, html_message=msg_html, fail_silently=True)

				return redirect('verify')

			except:
				res = redirect('signup')
				res.set_cookie('OSN_SIGNUP_ERROR', 'This Email is already taken')
				return res
				
		else:
			res = redirect('signup')
			res.set_cookie('OSN_SIGNUP_ERROR', "Passwords don't match")
			return res


@csrf_exempt
def checkSubdomain(request):
	subdomain = request.POST.get('subdomain')
	is_repeated = False

	if Company.objects.filter(subdomain=subdomain).exists():
		subdomain = subdomainModifier(subdomain)

	context = {
		"subdomain": subdomain,
		"domain": settings.SITE_DOMAIN,
	}

	return HttpResponse(json.dumps(context))