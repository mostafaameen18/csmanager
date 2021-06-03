from .__init__ import *

class signin(View):

	def get(self, request):

		if request.user.is_authenticated:
			if "next" in request.GET:
				return HttpResponseRedirect(request.GET['next'])
			return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
		
		context = {}

		if "next" in request.GET:
			context['next'] = request.GET['next']

		if "OSN_SIGNIN_ERROR" in request.COOKIES:
			err = request.COOKIES['OSN_SIGNIN_ERROR']
			context['err'] = err

		res = render(request, "signin.html", context)
		res.delete_cookie('OSN_SIGNIN_ERROR')
		return res

	def post(self, request):

		if request.user.is_authenticated:
			if "next" in request.GET:
				return HttpResponseRedirect(request.GET['next'])
			return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

		email = request.POST.get('email')
		password = request.POST.get('password')

		user = authenticate(username=email, password=password)
		if user is not None:
			login(request, user)
			if "next" in request.GET:
				return HttpResponseRedirect(request.GET['next'])
			return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

		else:
			if "next" in request.GET:
				res = HttpResponseRedirect('/accounts/signin?next={}'.format(request.GET['next']))
			else:
				res = redirect('signin')
			res.set_cookie('OSN_SIGNIN_ERROR', 'Wrong Username or Password')
			return res