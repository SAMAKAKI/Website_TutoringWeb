from django.contrib import admin
from .models import *

@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'mark', 'opinion']
