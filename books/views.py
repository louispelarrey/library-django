from django.shortcuts import render, redirect
from django import views
from books.models import Book, Author, Collection, Editor, Overdue, Category
from books.forms import AddBookForm, AddAuthorForm, AddCategoryForm, AddCollectionForm, AddEditorForm

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
            return redirect('books:books')
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
        return redirect('books:books')
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
        return redirect('books:books')
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
    return redirect('books:books')

def add_author(request):
    form = AddAuthorForm()
    if request.method == 'POST':
        name = request.POST['name']
        author = Author(name=name)
        author.save()
        return redirect('books:books')
    context = {
        'form': form
    }
    return render(request, 'author/add_author.html' , context)

def add_editor(request):
    form = AddEditorForm()
    if request.method == 'POST':
        name = request.POST['name']
        editor = Editor(name=name)
        editor.save()
        return redirect('books:books')
    context = {
        'form': form
    }
    return render(request, 'editor/add_editor.html' , context)

def add_collection(request):
    form = AddCollectionForm()
    if request.method == 'POST':
        name = request.POST['name']
        collection = Collection(name=name)
        collection.save()
        return redirect('books:books')
    context = {
        'form': form
    }
    return render(request, 'collection/add_collection.html' , context)

def add_category(request):
    form = AddCategoryForm()
    if request.method == 'POST':
        name = request.POST['name']
        category = Category(name=name)
        category.save()
        return redirect('books:book')
    context = {
        'form': form
    }
    return render(request, 'category/add_category.html' , context)