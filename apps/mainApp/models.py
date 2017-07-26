from __future__ import unicode_literals

from django.db import models
from ..login_app.models import Users
from datetime import date, datetime


class Dogs(models.Model):
    name = models.CharField(max_length=45)
    user = models.ForeignKey(Users, related_name='dog_Owner')
    size = models.CharField(max_length=45)
    breed = models.CharField(max_length=45)
    picture = models.CharField()

    created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Requests(models.Model):
    user = models.ForeignKey(Users, related_name='dog_Owner')
    inviter = models.ForeignKey(Users, related_name='dog_Inviter')
    created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Pals(models.Model):
    user = models.ForeignKey(Users, related_name='owner_Pals')
    pals = models.ForeignKey(Users, related_name='user_Pals')
    created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Messages
    user = models.ForeignKey(Users, related_name='user_Message')
    pal = models.ForeignKey(Pals, related_name='pal_Message')
    message = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Playdates
    user = models.ForeignKey(Users, related_name='owner_Playdate')
    pal = models.ForeignKey(Users, related_name='pal_Playdate')
    location = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
