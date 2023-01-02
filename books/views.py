from django.shortcuts import render, redirect
from django import views
from books.models import Book, Author, Collection, Editor, Overdue, Category, Library, Overdue
from libraries.models import Library, Bookseller
from books.forms import AddBookForm, AddAuthorForm, AddCategoryForm, AddCollectionForm, AddEditorForm
import datetime
from django.contrib.auth.models import User
import random

def book_index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'book/index.html', context)

def detail_book(request, id):
    book = Book.objects.get(id=id)
    libraries = Library.objects.filter(overdue__book=id, overdue__status='Disponible')
    context = {
        'book': book,
        'libraries': libraries,
    }
    return render(request, 'book/detail_book.html', context)

def random_reference():
    return random.randint(100000, 999999)

def get_reference():
    reference = random_reference()
    if Overdue.objects.filter(reference=reference).exists():
        return get_reference()
    else:
        return reference

def add_overdue(request, id):
    reference = get_reference()
    loan_date = datetime.datetime.now()
    due_date = datetime.datetime.now() + datetime.timedelta(days=7)

    book = Book.objects.get(id=id)
    user = User.objects.get(id=request.user.id)
    library = Library.objects.get(id=1)
    overdue = Overdue(reference=reference, loan_date=loan_date, due_date=due_date, book=book, user=user, library=library)

    overdue.save()
    return redirect('books:books')

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
        author = Author.objects.get(id=request.POST['author'])
        editor = Editor.objects.get(id=request.POST['editor'])
        collection = Collection.objects.get(id=request.POST['collection'])
        category = Category.objects.get(id=request.POST['category'])
        book = Book(title=title, description=description ,author=author, editor=editor, collection=collection, category=category)
        book.save()

        reference = get_reference()
        loan_date = datetime.datetime.now()
        due_date = datetime.datetime.now() + datetime.timedelta(days=7)
        status = 'Disponible'

        bookseller = Bookseller.objects.get(user=request.user.id)
        library = Library.objects.get(id=bookseller.library.id)
        
        overdue = Overdue(reference=reference, loan_date=loan_date, due_date=due_date, status=status, book=book, library=library)
        overdue.save()

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

def author_index(request):
    form = AddAuthorForm()
    authors = Author.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        author = Author(name=name)
        author.save()
        return redirect('books:authors')
    context = {
        'form': form,
        'authors': authors
    }
    return render(request, 'author/index.html' , context)

def editor_index(request):
    form = AddEditorForm()
    editors = Editor.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        editor = Editor(name=name)
        editor.save()
        return redirect('books:editors')
    context = {
        'form': form,
        'editors': editors
    }
    return render(request, 'editor/index.html' , context)

def collection_index(request):
    form = AddCollectionForm()
    collections = Collection.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        collection = Collection(name=name)
        collection.save()
        return redirect('books:collections')
    context = {
        'form': form,
        'collections': collections
    }
    return render(request, 'collection/index.html' , context)

def category_index(request):
    form = AddCategoryForm()
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        category = Category(name=name)
        category.save()
        return redirect('books:categories')
    context = {
        'form': form,
        'categories': categories
    }
    return render(request, 'category/index.html' , context)