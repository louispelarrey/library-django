from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_index , name='books'),

    path('add_book/', views.add_book, name='add_book'),
    path('detail_book/<int:id>', views.detail_book, name='detail_book'),

    path('add_overdue/<int:id>', views.add_overdue, name='add_overdue'),

    path('authors/', views.author_index, name='authors'),

    path('editors/', views.editor_index, name='editors'),

    path('collections/', views.collection_index, name='collections'),

    path('categories/', views.category_index, name='categories'),
]