from django.db import models
from django.db.models.enums import Choices
from accounts.models import Company, User

class Branch(models.Model):
    typeChoices = (
        ('choice', 'Choice'),
        ('dial', 'Dial'),
    )
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=500, choices=typeChoices)
    message = models.TextField()
    number = models.CharField(max_length=500)


class Choice(models.Model):
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.SET_NULL)
    branch = models.ForeignKey(Branch, blank=True, null=True, on_delete=models.SET_NULL)
    message = models.CharField(max_length=500)
    number = models.IntegerField()
    reference = models.ForeignKey(Branch, blank=True, null=True, on_delete=models.SET_NULL, related_name='reference')


class Answer(models.Model):
    company = models.OneToOneField(Company, blank=True, null=True, on_delete=models.SET_NULL)
    message = models.TextField()
    redirect = models.ForeignKey(Branch, blank=True, null=True, on_delete=models.SET_NULL)
    