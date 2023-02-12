from django.contrib import admin
from .models import Book, Author, Editor, Collection, Category

admin.site.register(Author)
admin.site.register(Editor)
admin.site.register(Collection)
admin.site.register(Category)
