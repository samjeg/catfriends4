# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class UserProfileInfo(models.Model):
	user = models.OneToOneField(User, related_name='userprofileinfos', on_delete=models.CASCADE, blank=True, null=True, default=1)
	picture = models.ImageField(upload_to='images', blank=True, null=True)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('cat_app:profile_detail', kwargs={'pk':self.pk})

class Cat_Topic(models.Model):
	owner = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, blank=True, null=True)
	cat_name = models.CharField(max_length=20)
	cat_picture = models.ImageField(upload_to='cat_images', blank=True, null=True)
	story = models.CharField(max_length=140)

	def __str__(self):
		return self.cat_name

	def get_absolute_url(self):
		return reverse('cat_app:cat_detail', kwargs={'pk':self.pk})

class Cat_Topic_Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	cat_topic = models.ForeignKey(Cat_Topic, related_name="comments", on_delete=models.CASCADE, blank=True, null=True)
	comment = models.CharField(max_length=140)
	comment_picture_path = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.user.username
