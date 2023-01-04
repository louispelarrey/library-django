from django.shortcuts import render, redirect
from .models import Library
from books.models import Overdue
from django.contrib.auth.models import User

# Create your views here.
def libraries(request):
    libraries = Library.objects.all()
    context = {
        'libraries': libraries
    }
    return render(request, 'map/libraries.html', context)

def library_index(request):
    libraries = Library.objects.all()
    context = {
        'libraries': libraries
    }
    return render(request, 'library/index.html', context)
    
def library_detail(request, slug):
    library = Library.objects.get(slug=slug)
    overdues = Overdue.objects.filter(library=library)
    context = {
        'library': library,
        'overdues': overdues,
    }
    return render(request, 'library/detail.html', context)
