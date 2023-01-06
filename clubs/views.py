from django.shortcuts import render, redirect
from django import views
from clubs.models import Club, Session, Member
from libraries.models import Library, Bookseller
from django.contrib.auth.models import User


def club_index(request):
    clubs = Club.objects.all()
    context = {
        'clubs': clubs
    }
    return render(request, 'club/index.html', context)

