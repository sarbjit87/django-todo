# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView
from .forms import RegisterUserForm

class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'accounts/register.html'
    success_url = '/'
