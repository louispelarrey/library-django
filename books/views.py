from django.shortcuts import render, redirect
from django import views
from books.models import Book, Author, Collection, Editor, Overdue, Category, Library, Overdue
from libraries.models import Library, Bookseller
from books.forms import AddBookForm, AddAuthorForm, AddCategoryForm, AddCollectionForm, AddEditorForm

def book_index(request):
    overdues = Overdue.objects.all()

    context = {
        'overdues': overdues
    }
    return render(request, 'book/index.html', context)

def detail_book(request, id):
    book = Book.objects.get(id=id)
    libraries = Library.objects.filter(overdue__book=id, overdue__status='Disponible')
    bookseller = Bookseller.objects.get(user=request.user)
    library = Library.objects.get(id=bookseller.library.id)
    overdues = Overdue.objects.filter(book=id, library=library.id)
    
    context = {
        'book': book,
        'libraries': libraries,
        'library': library,
        'bookseller': bookseller,
        'overdues': overdues,
    }
    return render(request, 'book/detail_book.html', context)

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