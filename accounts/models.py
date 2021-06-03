from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=500)
	subdomain = models.CharField(max_length=500, unique=True)
	image = models.FileField(blank=True, null=True)
	dateCreated = models.DateTimeField(auto_now_add=True)
	phoneNumber = models.CharField(max_length=500, blank=True, null=True)
	code = models.CharField(max_length=500, blank=True, null=True)

	def __str__(self):
		return "{}_{}".format(self.id, self.user.username)