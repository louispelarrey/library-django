from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from books.models import Book, Overdue
from libraries.models import Library, Bookseller
from clubs.models import Club, Session, Member, Participant
from books.models import Book, Author, Collection, Editor, Overdue, Category, Library, Overdue
from books.forms import AddBookForm
from clubs.forms import AddClubForm, AddSessionForm
import datetime, random, json
from django.utils import timezone

def my_profile(request, username):
    try:
        user = User.objects.get(username=username)
        context = {'user': user}
        return render(request, 'my_profile/index.html', context)
    except:
        return redirect('home-index')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('members:dashboard')
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
            overdues_in_calendar = []
            for overdue in overdues:
                date = overdue.due_date
                overdues_in_calendar.append({
                    'title': overdue.book.title,
                    'start': date.isoformat(),
                    'end': date.isoformat(),
                    'url': '/books/detail_book/' + str(overdue.book.pk)
            })

            clubs = Club.objects.filter(library=library)
            for club in clubs:
                club.members_count = Member.objects.filter(club=club).count()
            books = []
            for overdue in overdues:
                books.append(overdue.book)
            context = {
                'library': library,
                'books': books,
                'overdues': overdues,
                'overdues_late': overdues_late,
                'overdues_in_calendar': json.dumps(overdues_in_calendar),
                'clubs': clubs
            }
            return render(request, 'dashboard/bookseller.html', context)
        else:
            overdues = Overdue.objects.filter(user=request.user)
            overdues_late = overdues.filter(due_date__lt=timezone.now())

            overdues_in_calendar = []
            for overdue in overdues:
                date = overdue.due_date
                overdues_in_calendar.append({
                    'title': overdue.book.title,
                    'start': date.isoformat(),
                    'end': date.isoformat(),
            })

            members = Member.objects.filter(user=request.user)
            clubs = []
            for member in members:
                clubs.append(member.club)

            sessions = Session.objects.filter(club__in=clubs)
            sessions_in_calendar = []
            for session in sessions:
                end = session.date + datetime.timedelta(hours=1)
                sessions_in_calendar.append({
                    'title': session.club.name,
                    'start': session.date.isoformat(),
                    'end': end.isoformat(),
                })

            context = {
                'overdues_late': overdues_late,
                'overdues_in_calendar': json.dumps(overdues_in_calendar),
                'sessions_in_calendar': json.dumps(sessions_in_calendar)
            }
            return render(request, 'dashboard/user.html', context)
    else:
        return redirect('members:login')

######################################### USERS #########################################

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

def my_clubs(request):
    members = Member.objects.filter(user=request.user)
    clubs = []
    for member in members:
        clubs.append(member.club)
        
    for club in clubs:
        club.members_count = Member.objects.filter(club=club).count()

    participants = Participant.objects.filter(user=request.user)
    sessions = []
    for participant in participants:
        sessions.append(participant.session)

    context = {
        'clubs': clubs,
        'sessions': sessions
    }
    return render(request, 'my_club/index.html', context)

def join_club(request, club_id):
    club = Club.objects.get(id=club_id)
    member = Member(club=club, user=request.user)
    member.save()
    return redirect('members:user_clubs')

def leave_club(request, club_id):
    club = Club.objects.get(id=club_id)
    member = Member.objects.get(club=club, user=request.user)
    member.delete()
    sessions = Session.objects.filter(club=club)
    for session in sessions:
        try:
            participant = Participant.objects.get(session=session, user=request.user)
            participant.delete()
        except:
            pass
    return redirect('members:user_clubs')

def join_session(request, session_id):
    session = Session.objects.get(id=session_id)
    participant = Participant(session=session, user=request.user)
    participant.save()
    return redirect('members:user_clubs')

def leave_session(request, session_id):
    session = Session.objects.get(id=session_id)
    participant = Participant.objects.get(session=session, user=request.user)
    participant.delete()
    return redirect('members:user_clubs')

######################################### BOOKSELLER #########################################

def my_library(request):
    bookseller = Bookseller.objects.get(user=request.user)
    library = Library.objects.get(id=bookseller.library.id)
    overdues = Overdue.objects.filter(library=library)
    clubs = Club.objects.filter(library=library)
    for club in clubs:
        club.members_count = Member.objects.filter(club=club).count()
    books = []
    for overdue in overdues:
        book = Book.objects.get(id=overdue.book.id)
        books.append(book)

    context = {
        'books': books,
        'clubs': clubs,
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
    form = AddBookForm(request.FILES or None)
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
        cover = request.FILES['cover']
        book = Book(title=title, description=description ,cover=cover , author=author, editor=editor, collection=collection, category=category)
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

def show_club(request, club_id):
    club = Club.objects.get(id=club_id)
    club.members_count = Member.objects.filter(club=club).count()
    members = Member.objects.filter(club=club)
    sessions = Session.objects.filter(club=club)
    sessions_in_calendar = []
    for session in sessions:
        end = session.date + datetime.timedelta(hours=1)
        sessions_in_calendar.append({
            'title': session.club.name,
            'start': session.date.isoformat(),
            'end': end.isoformat(),
            'url': '/members/sessions/' + str(session.pk)
        })

    form = AddSessionForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('members:show_club', club_id=str(session.club.pk))
        else:
            form = AddSessionForm()

        date = request.POST['date']
        session = Session(date=date, club=club)
        session.save()
        return redirect('members:show_club', club_id=str(session.club.pk))

    context = {
        'club': club,
        'members': members,
        'sessions': sessions,
        'sessions_in_calendar': json.dumps(sessions_in_calendar),
        'form': form
    }
    return render(request, 'my_library/show_club.html', context)

def add_club(request):
    form = AddClubForm()
    bookseller = Bookseller.objects.get(user=request.user.id)
    library = Library.objects.get(id=bookseller.library.id)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('members:user_library')
        else:
            form = AddClubForm()

        name = request.POST['name']
        description = request.POST['description']
        capacity = request.POST['capacity']

        books = Book.objects.get(id=request.POST['book'])

        club = Club(name=name, description=description, capacity=capacity, library=library, book=books)
        club.save()
        return redirect('members:user_library')

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

def delete_member(request, member_id):
    member = Member.objects.get(id=member_id)
    member.delete()
    return redirect('members:user_clubs')

def show_session(request, session_id):
    session = Session.objects.get(id=session_id)
    participants = Participant.objects.filter(session=session)
    context = {
        'session': session,
        'participants': participants
    }
    return render(request, 'my_library/show_session.html', context)

def delete_session(request, session_id):
    session = Session.objects.get(id=session_id)
    session.delete()
    return redirect('members:show_club', club_id=session.club.pk)

def delete_participant(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    participant.delete()
    return redirect('members:user_library')