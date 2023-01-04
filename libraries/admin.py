# admin.py
from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import Library, Bookseller


admin.site.register(Library, LeafletGeoAdmin)
admin.site.register(Bookseller)