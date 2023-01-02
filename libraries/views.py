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

def library_detail(request, id):
    library = Library.objects.get(id=id)
    overdues = Overdue.objects.filter(library=library)
    context = {
        'library': library,
        'overdues': overdues,
    }
    return render(request, 'library/detail.html', context)

def edit_overdue(request, id):
    overdue = Overdue.objects.get(id=id)
    overdue.user = User.objects.get(id=request.user.id)
    overdue.status = 'Indisponible'
    overdue.save()
    return redirect('libraries:libraries')