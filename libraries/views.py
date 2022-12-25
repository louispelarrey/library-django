from django.shortcuts import render
from .models import Library

# Create your views here.
def libraries(request):
    libraries = Library.objects.all()
    context = {
        'libraries': libraries
    }
    return render(request, 'map/libraries.html', context)