from django.contrib import admin
from .models import Form
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Form)
# @admin.register(Form)
# class FormAdmin(UserAdmin):
#     list_display=['email','full_name','age']
