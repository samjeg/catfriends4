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

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		profiles = models.UserProfileInfo.objects.all()
		user = self.request.user
		if user.is_authenticated:
			for profile in profiles:
				if user.id == profile.user.id:
					context['profile_detail'] = profile
		return context

class UserProfileDetailView(DetailView):
	context_object_name = 'profile_detail'
	model = models.UserProfileInfo
	template_name = 'cat_app/profile_detail.html'

class UserProfileCreateView(CreateView):
	fields = ('user', 'picture')
	model = models.UserProfileInfo
	template_name = 'cat_app/profile_create.html'

	def get_context_data(self, **kwargs):
		context = super(UserProfileCreateView, self).get_context_data(**kwargs)
		profiles = models.UserProfileInfo.objects.all()
		user = self.request.user
		if user.is_authenticated:
			for profile in profiles:
				if user.id == profile.user.id:
					context['profile_detail'] = profile
		return context

class UserProfileUpdateView(UpdateView):
	fields = ('picture',)
	model = models.UserProfileInfo
	template_name = 'cat_app/profile_create.html'

	def get_context_data(self, **kwargs):
		context = super(UserProfileUpdateView, self).get_context_data(**kwargs)
		profiles = models.UserProfileInfo.objects.all()
		user = self.request.user
		if user.is_authenticated:
			for profile in profiles:
				if user.id == profile.user.id:
					context['profile_detail'] = profile
		return context

class UserProfileDeleteView(DeleteView):
	context_object_name = 'profile_detail'
	model = models.UserProfileInfo
	success_url = reverse_lazy('index')
	template_name = 'cat_app/profile_delete_confirm.html'

class CatListView(ListView):
	model = models.Cat_Topic
	template_name = 'cat_app/cat_list.html'

	def get_context_data(self, **kwargs):
		context = super(CatListView, self).get_context_data(**kwargs)
		context['cat_list'] = self.object_list
		profiles = models.UserProfileInfo.objects.all()
		user = self.request.user
		if user.is_authenticated:
			for profile in profiles:
				if user.id == profile.user.id:
					context['profile_detail'] = profile
		return context

class CatDetailView(DetailView):
	model = models.Cat_Topic
	template_name = 'cat_app/cat_detail.html'

	def get_context_data(self, **kwargs):
		context = super(CatListView, self).get_context_data(**kwargs)
		context['cat_detail'] = self.get_object()
		profiles = models.UserProfileInfo.objects.all()
		user = self.request.user
		if user.is_authenticated:
			for profile in profiles:
				if user.id == profile.user.id:
					context['profile_detail'] = profile
		return context

class CatCreateView(CreateView):
	fields = ('owner', 'cat_name', 'cat_picture', 'story')
	model = models.Cat_Topic
	template_name = 'cat_app/create_cat.html'

	def get_context_data(self, **kwargs):
		context = super(CatCreateView, self).get_context_data(**kwargs)
		context['cat_detail'] = self.get_object()
		profiles = models.UserProfileInfo.objects.all()
		user = self.request.user
		if user.is_authenticated:
			for profile in profiles:
				if user.id == profile.user.id:
					context['profile_detail'] = profile
		return context

class CatUpdateView(UpdateView):
	fields = ('cat_name', 'cat_picture', 'story')
	model = models.Cat_Topic
	template_name = 'cat_app/create_cat.html'

	def get_context_data(self, **kwargs):
		context = super(CatUpdateView, self).get_context_data(**kwargs)
		context['cat_detail'] = self.get_object()
		profiles = models.UserProfileInfo.objects.all()
		user = self.request.user
		if user.is_authenticated:
			for profile in profiles:
				if user.id == profile.user.id:
					context['profile_detail'] = profile
		return context

class CatDeleteView(DeleteView):
	model = models.Cat_Topic
	success_url = reverse_lazy('index')
	template_name = 'cat_app/cat_delete_confirm.html'

	def get_context_data(self, **kwargs):
		context = super(CatDeleteView, self).get_context_data(**kwargs)
		context['cat_detail'] = self.get_object()
		profiles = models.UserProfileInfo.objects.all()
		user = self.request.user
		if user.is_authenticated:
			for profile in profiles:
				if user.id == profile.user.id:
					context['profile_detail'] = profile
		return context


