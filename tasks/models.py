# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    owner           = models.ForeignKey(User,related_name='user_owner')
    name            = models.CharField(max_length=120)
    description     = models.TextField()
    PRIORITY_CHOICES = (
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High")
    )
    priority        = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="Low")
    assignee        = models.ForeignKey(User,related_name='user_assignee')
    created_on      = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True)
    due_on          = models.DateTimeField(null=True, blank=True)
    slug            = models.SlugField(null=True, blank=True)
