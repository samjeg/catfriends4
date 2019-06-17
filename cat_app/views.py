# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
									TemplateView, 
									DetailView,
									CreateView,
									UpdateView,
								)
from . import models
from . import forms

class Register(CreateView):
    form_class = forms.UserCreateForm
    template_name = "cat_app/register.html"
    success_url = reverse_lazy("index")

class IndexView(TemplateView):
	template_name = 'cat_app/index.html'

class UserProfileDetailView(DetailView):
	context_object_name = 'profile_detail'
	model = models.UserProfileInfo
	template_name = 'cat_app/profile_detail.html'

class UserProfileCreateView(CreateView):
	fields = ('user', 'picture')
	model = models.UserProfileInfo
	template_name = 'cat_app/profile_create.html'

class UserProfileUpdateView(UpdateView):
	fields = ('picture',)
	model = models.UserProfileInfo
	template_name = 'cat_app/profile_create.html'

