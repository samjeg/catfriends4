# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
									TemplateView, 
									DetailView,
									CreateView,
									UpdateView,
									DeleteView,
									ListView,
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

class UserProfileDeleteView(DeleteView):
	context_object_name = 'profile'
	model = models.UserProfileInfo
	success_url = reverse_lazy('index')
	template_name = 'cat_app/profile_delete_confirm.html'

class CatListView(ListView):
	context_object_name = 'cat_list'
	model = models.Cat_Topic
	template_name = 'cat_app/cat_list.html'

class CatDetailView(DetailView):
	context_object_name = 'cat_detail'
	model = models.Cat_Topic
	template_name = 'cat_app/cat_detail.html'

class CatCreateView(CreateView):
	fields = ('owner', 'cat_name', 'cat_picture', 'story')
	model = models.Cat_Topic
	template_name = 'cat_app/create_cat.html'

class CatUpdateView(UpdateView):
	fields = ('cat_name', 'cat_picture', 'story')
	model = models.Cat_Topic
	template_name = 'cat_app/create_cat.html'

class CatDeleteView(DeleteView):
	context_object_name = 'cat'
	model = models.Cat_Topic
	success_url = reverse_lazy('index')
	template_name = 'cat_app/cat_delete_confirm.html'


