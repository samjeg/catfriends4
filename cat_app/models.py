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

