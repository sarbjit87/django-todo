# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    age       = models.IntegerField(blank=True,null=True)
    country   = models.CharField(max_length=15,blank=True,null=True)
