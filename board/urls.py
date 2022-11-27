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

app_name = 'board'

urlpatterns = [
    path('', views.board, name='board'),
    path('<int:id>/', views.topic, name='topic'),
    path('<int:topic_id>/delete_post/<int:message_id>/', views.delete_post, name='delete_post'),
    path('delete_topic/<int:id>', views.delete_topic, name='delete_topic'),
]
