from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_index , name='books'),
    path('add_book/', views.add_book, name='add_book'),
    path('delete_book/<int:id>', views.delete_book, name='delete_book'),
    path('edit_book/<int:id>', views.edit_book, name='edit_book'),

    path('add_author/', views.add_author, name='add_author'),

    path('add_editor/', views.add_editor, name='add_editor'),

    path('add_collection/', views.add_collection, name='add_collection'),

    path('add_category/', views.add_category, name='add_category'),
]