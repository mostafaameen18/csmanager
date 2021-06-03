from .__init__ import *

def signout(request):
	logout(request)
	return redirect('signin')