from django.urls import path, include
from .views import home_index

urlpatterns = [
    path('', home_index, name='home-index'),
]