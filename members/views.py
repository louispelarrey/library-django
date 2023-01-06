from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from books.models import Book, Overdue
from libraries.models import Library, Bookseller
from clubs.models import Club, Session, Member
from books.models import Book, Author, Collection, Editor, Overdue, Category, Library, Overdue
from books.forms import AddBookForm
from clubs.forms import AddClubForm, AddSessionForm
import datetime, random
from django.utils import timezone

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('board:board')
        else:
            messages.error(request, 'Le nom de compte ou le mot de passe est incorrect')
    context = {}
    return render(request, 'authenticate/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('members:login')

def register_user(request):
    try :
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('members:login')
    except IntegrityError:
        messages.error(request, 'Le nom de compte existe déjà')
    except :
        messages.error(request, 'Une erreur est survenue')
    context = {}
    return render(request, 'authenticate/register.html', context)

def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            bookseller = Bookseller.objects.get(user=request.user)
            library = Library.objects.get(id=bookseller.library.id)
            overdues = Overdue.objects.filter(library=library)
            overdues_late = overdues.filter(due_date__lt=timezone.now())
            books = []
            for overdue in overdues:
                books.append(overdue.book)
            context = {
                'library': library,
                'books': books,
                'overdues': overdues,
                'overdues_late': overdues_late
            }
            return render(request, 'dashboard/bookseller.html', context)
        else:
            return render(request, 'dashboard/user.html')
    else:
        return redirect('members:login')

######################################### USERS #########################################

def bookseller_dashboard(request):
    return render(request, 'dashboard/bookseller.html')

def my_books(request):
    overdues = Overdue.objects.filter(user=request.user)
    overdues_late = overdues.filter(due_date__lt=timezone.now())

    context = {
        'overdues': overdues,
        'overdues_late': overdues_late
    }

    return render(request, 'my_book/index.html', context)

def add_overdue(request, reference):
    overdue = Overdue.objects.get(reference=reference)
    overdue.loan_date = datetime.datetime.now()
    overdue.due_date = datetime.datetime.now() + datetime.timedelta(days=7)
    overdue.status = 'Indisponible'
    overdue.user = User.objects.get(id=request.user.id)
    overdue.save()
    return redirect('books:books')
    
def edit_overdue(request, reference):
    overdue = Overdue.objects.get(reference=reference)
    overdue.status = 'Disponible'
    overdue.user = None
    overdue.save()
    return redirect('members:user_books')

def join_club(request, id):
    club = Club.objects.get(id=id)
    member = Member(club=club, user=request.user)
    member.save()
    return redirect('clubs:clubs')

######################################### BOOKSELLER #########################################

def my_library(request):
    bookseller = Bookseller.objects.get(user=request.user)
    library = Library.objects.get(id=bookseller.library.id)
    overdues = Overdue.objects.filter(library=library)
    books = []
    for overdue in overdues:
        book = Book.objects.get(id=overdue.book.id)
        books.append(book)

    context = {
        'books': books
    }
    return render(request, 'my_library/index.html', context)

def random_reference():
    return random.randint(100000, 999999)

def get_reference():
    reference = random_reference()
    if Overdue.objects.filter(reference=reference).exists():
        return get_reference()
    else:
        return reference

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

        return redirect('members:user_library')
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
    return render(request, 'my_library/add_book.html', context)

def my_clubs(request):
    user = request.user
    bookseller = Bookseller.objects.get(user=user)
    library = Library.objects.get(bookseller=bookseller)
    clubs = Club.objects.filter(library=library)
    context = {
        'clubs': clubs
    }
    return render(request, 'my_library/clubs.html', context)

def add_club(request):
    form = AddClubForm()
    bookseller = Bookseller.objects.get(user=request.user.id)
    library = Library.objects.get(id=bookseller.library.id)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('members:user_clubs')
        else:
            form = AddClubForm()

        name = request.POST['name']
        description = request.POST['description']
        capacity = request.POST['capacity']

        books = Book.objects.get(id=request.POST['book'])

        club = Club(name=name, description=description, capacity=capacity, library=library, book=books)
        club.save()
        return redirect('members:user_clubs')

    overdues = Overdue.objects.filter(library=library)
    books = []
    for overdue in overdues:
        book = Book.objects.get(id=overdue.book.id)
        books.append(book)
    context = {
        'books': books,
        'form': form
    }
    return render(request, 'my_library/add_club.html', context)