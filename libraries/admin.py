# admin.py
from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import Library


admin.site.register(Library, LeafletGeoAdmin)