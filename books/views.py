from django.shortcuts import render, redirect
from django import views
from books.models import Book, Author, Collection, Editor, Overdue, Category

def book_index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'book/index.html', context)

