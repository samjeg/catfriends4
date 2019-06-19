# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserProfileInfo, Cat_Topic, Cat_Topic_Comment

admin.site.register(UserProfileInfo)
admin.site.register(Cat_Topic)
admin.site.register(Cat_Topic_Comment)
