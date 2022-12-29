from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_index , name='books'),

    path('add_book/', views.add_book, name='add_book'),
    path('delete_book/<int:id>', views.delete_book, name='delete_book'),
    path('edit_book/<int:id>', views.edit_book, name='edit_book'),

    path('add_overdue/<int:id>', views.add_overdue, name='add_overdue'),

    path('authors/', views.author_index, name='authors'),

    path('editors/', views.editor_index, name='editors'),

    path('collections/', views.collection_index, name='collections'),

    path('categories/', views.category_index, name='categories'),
]