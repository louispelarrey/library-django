from django.urls import path
from . import views

app_name = 'clubs'

urlpatterns = [
    path('clubs/', views.club_index , name='clubs'),
    path('clubs/<int:club_id>', views.detail_club, name='detail_club'),
]