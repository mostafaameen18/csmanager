from .__init__ import *

class verify(View):

	def get(self, request):

		if request.user.is_authenticated:
			return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

		context = {}

		if "OSN_VERIFY_ERROR" in request.COOKIES:
			err = request.COOKIES['OSN_VERIFY_ERROR']
			context['err'] = err

		res = render(request, "verify.html", context)
		res.delete_cookie('OSN_VERIFY_ERROR')
		return res

	def post(self, request):

		if request.user.is_authenticated:
			return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

		code = request.POST['code']

		try:
			company = Company.objects.get(code=code)

			user = company.user
			user.is_active = True
			user.save()

			company.code = ''
			company.save()

			return redirect('signin')

		except:
			res = redirect('verify')
			res.set_cookie('OSN_VERIFY_ERROR', 'Please, Enter Code Sent To Your Email Address')
			return res
		