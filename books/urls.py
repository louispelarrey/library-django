from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_index , name='books'),

    path('detail_book/<int:id>', views.detail_book, name='detail_book'),
]