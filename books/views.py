from django.shortcuts import render, redirect
from django import views
from books.models import Book, Author, Collection, Editor, Overdue, Category
from books.forms import AddBookForm

def book_index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'book/index.html', context)

def add_book(request):
    form = AddBookForm()
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            return redirect('books:book_index')
        else:
            form = AddBookForm()

        title = request.POST['title']
        description = request.POST['description']
        author = request.POST['author']
        editor = request.POST['editor']
        collection = request.POST['collection']
        category = request.POST['category']
        book = Book(title=title, description=description ,author=author, editor=editor, collection=collection, category=category)
        book.save()
        return redirect('books:book_index')
    authors = Author.objects.all()
    editors = Editor.objects.all()
    collections = Collection.objects.all()
    categories = Category.objects.all()
    context = {
        'authors': authors,
        'editors': editors,
        'collections': collections,
        'categories': categories,
        'form': form
    }
    return render(request, 'book/add_book.html', context)

def edit_book(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        editor = request.POST['editor']
        collection = request.POST['collection']
        category = request.POST['category']
        isbn = request.POST['isbn']
        book = Book.objects.get(id=id)
        book.title = title
        book.author = author
        book.editor = editor
        book.collection = collection
        book.category = category
        book.isbn = isbn
        book.save()
        return redirect('books:book_index')
    book = Book.objects.get(id=id)
    authors = Author.objects.all()
    editors = Editor.objects.all()
    collections = Collection.objects.all()
    categories = Category.objects.all()
    context = {
        'book': book,
        'authors': authors,
        'editors': editors,
        'collections': collections,
        'categories': categories
    }
    return render(request, 'book/edit_book.html', context)

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books:book_index')
