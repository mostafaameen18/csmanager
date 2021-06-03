from django.urls import path, include
# from accounts.views.__init__ import VIEW_NAME
from . import signin
from . import signup
from . import verify
from . import signout

urlpatterns = [
	path('',include(signin)),
	path('',include(signup)),
	path('',include(verify)),
	path('',include(signout)),
]