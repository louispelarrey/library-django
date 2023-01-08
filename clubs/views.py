from django.shortcuts import render, redirect
from django import views
from clubs.models import Club, Session, Member
from libraries.models import Library, Bookseller
from django.contrib.auth.models import User, Group


def club_index(request):
    clubs = Club.objects.all()
    context = {
        'clubs': clubs
    }
    return render(request, 'club/index.html', context)

def detail_club(request, club_id):
    club = Club.objects.get(id=club_id)
    sessions = Session.objects.filter(club=club)
    members = Member.objects.filter(club=club)
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        is_member = Member.objects.filter(user=user, club=club)
    else:
        is_member = None

    context = {
        'club': club,
        'sessions': sessions,
        'members': members,
        'is_member': is_member
    }
    return render(request, 'club/detail_club.html', context)

