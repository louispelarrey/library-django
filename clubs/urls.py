from django.urls import path
from . import views

app_name = 'clubs'

urlpatterns = [
    path('clubs/', views.club_index , name='clubs'),
]