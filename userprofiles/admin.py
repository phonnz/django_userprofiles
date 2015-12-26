# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdmin(UserAdmin):
	change_list_template = "admin/change_list_filter_sidebar.html"
	list_display = ['username', 'email', 'first_name', 'last_name', 'last_login', 'created', 'is_staff','is_active' ]
	list_editable = ('is_active',)
	fieldsets=(
		('Usuario', {'fields':('username', 'email', 'password' )}),
		('Datos personales', {'fields':('first_name', 'last_name', 'mom_last_name' )}),
		('Permisos', {'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		)
	list_filter = ('created','is_active', 'last_login', 'is_staff')
	search_fields = ('username', 'email')

admin.site.register(User, UserAdmin)
