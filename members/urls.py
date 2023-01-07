"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('my_books/', views.my_books, name='user_books'),
    path('my_books/<str:reference>/add', views.add_overdue, name='add_overdue'),
    path('my_books/<str:reference>/giveback', views.edit_overdue, name='edit_overdue'),
    path('clubs/join/<int:club_id>', views.join_club, name='join_club'),

    path('my_library/', views.my_library, name='user_library'),
    path('add_book/', views.add_book, name='add_book'),

    path('my_clubs/', views.my_clubs, name='user_clubs'),
    path('my_clubs/<int:club_id>', views.show_club, name='show_club'),
    path('my_clubs/add', views.add_club, name='add_club'),

    path('my_sessions/<int:session_id>', views.show_session, name='show_session'),
    path('my_sessions/<int:club_id>/add', views.add_session, name='add_session'),
    path('my_sessions/<int:session_id>/delete', views.delete_session, name='delete_session')
]
