from django.contrib import admin
from tur.models import *

@admin.register(cuenta)
class cuenta(admin.ModelAdmin):
    list_display = ('usuario','password')
    pass