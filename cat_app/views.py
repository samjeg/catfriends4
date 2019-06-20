# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseForbidden
from django.urls import reverse
from django import forms as django_forms
from django.views.generic import (
									TemplateView, 
									DetailView,
									CreateView,
									UpdateView,
									DeleteView,
									ListView,
								)
from django.views.generic.edit import FormMixin
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
	fields = ('user', 'picture',)
	model = models.UserProfileInfo
	template_name = 'cat_app/profile_create.html'

	def get_context_data(self, **kwargs):
		context = super(UserProfileCreateView, self).get_context_data(**kwargs)
		profiles = models.UserProfileInfo.objects.all()
		user = self.request.user
		form = self.get_form()
		if user.is_authenticated:
			form.initial['user'] = user.id
			form.fields['user'].widget = django_forms.HiddenInput()
			context['profile_form'] = form
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
		form = self.get_form()
		if user.is_authenticated:
			context['profile_form'] = form
			for profile in profiles:
				if user.id == profile.user.id:
					context['profile_detail'] = profile


		return context

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

class CatDetailView(FormMixin, DetailView):
	model = models.Cat_Topic
	template_name = 'cat_app/cat_detail.html'
	form_class = forms.CatCommentForm

	def get_success_url(self):
		return reverse_lazy('cat_app:cat_detail', kwargs={'pk': self.object.pk})

	def get_context_data(self, **kwargs):
		context = super(CatDetailView, self).get_context_data(**kwargs)
		form = self.get_form()
		context['cat_detail'] = self.get_object()
		cat_topic = self.get_object()
		profiles = models.UserProfileInfo.objects.all()
		user = self.request.user
		if user.is_authenticated:
			for profile in profiles:
				if user.id == profile.user.id:
					context['profile_detail'] = profile
					form.initial['user'] = user.id
					form.initial['cat_topic'] = cat_topic.id
					form.initial['comment_picture_path'] = profile.picture
					context['form'] = form
		return context

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return HttpResponseForbidden()
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		new_comment = models.Cat_Topic_Comment(
			user = form.cleaned_data['user'],
			cat_topic = form.cleaned_data['cat_topic'],
			comment = form.cleaned_data['comment'],
			comment_picture_path = form.cleaned_data['comment_picture_path']
		)

		new_comment.save()
		
		return super(CatDetailView, self).form_valid(form)

class CatCreateView(CreateView):
	fields = ('owner', 'cat_name', 'cat_picture', 'story')
	model = models.Cat_Topic
	template_name = 'cat_app/create_cat.html'

	def get_context_data(self, **kwargs):
		context = super(CatCreateView, self).get_context_data(**kwargs)
		user = self.request.user
		profiles = models.UserProfileInfo.objects.all()
		form = self.get_form()
		if user.is_authenticated:
			for profile in profiles:
				if user.id == profile.user.id:
					context['profile_detail'] = profile
					form.initial['owner'] = user.id
					form.fields['owner'].widget = django_forms.HiddenInput()
					context['cat_form'] = form
		return context

class CatUpdateView(UpdateView):
	fields = ('cat_name', 'cat_picture', 'story')
	model = models.Cat_Topic
	template_name = 'cat_app/create_cat.html'

	def get_context_data(self, **kwargs):
		context = super(CatUpdateView, self).get_context_data(**kwargs)
		profiles = models.UserProfileInfo.objects.all()
		user = self.request.user
		form = self.get_form()
		if user.is_authenticated:
			for profile in profiles:
				if user.id == profile.user.id:
					context['profile_detail'] = profile
					context['cat_form'] = form
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


