from atexit import register
from django.contrib import admin
from . import models

@admin.register(models.House)
class HouseAdmin(admin.ModelAdmin):

    pass
