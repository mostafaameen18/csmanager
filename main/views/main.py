from .__init__ import *

def main(request):
	
	context = {}

	if request.user.is_authenticated:
		company = Company.objects.get(user=request.user)
		context['company'] = company
	
	return render(request, "main.html", context)