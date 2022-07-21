from django.contrib import admin
from .models import dictionary
# Register your models here.

class AdminDic(admin.ModelAdmin):
    list_display = ['chinese','english']

admin.site.register(dictionary, AdminDic)
