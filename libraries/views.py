from django.shortcuts import render
from .models import Library
from books.models import Overdue

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
