# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from bonito.models import temperatura

# registro de modelos
class TemperaturaAdmin(admin.ModelAdmin):
    list_display = ("fecha", "temperatura")
    ordering = ("fecha","temperatura")

admin.site.register(temperatura, TemperaturaAdmin)
