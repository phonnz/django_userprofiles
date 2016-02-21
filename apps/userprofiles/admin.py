# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdmin(UserAdmin):
	change_list_template = "admin/change_list_filter_sidebar.html"
	list_display = ['username', 'email', 'name', 'date_joined', 'last_login', 'is_staff','is_active' ]
	list_editable = ('is_active',)
	fieldsets=(
		('Usuario', {'fields':('username', 'slug', 'email', 'password', 'points' )}),
		('Datos personales', {'fields':('name', )}),
		('Permisos', {'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		)
	list_filter = ('date_joined','is_active', 'last_login', 'is_staff')
	search_fields = ('username', 'email')

admin.site.register(User, UserAdmin)
