# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
	model = CustomUser
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	
admin.site.register(CustomUser, CustomUserAdmin)
