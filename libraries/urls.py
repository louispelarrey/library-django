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
from djgeojson.views import GeoJSONLayerView
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Library

app_name = 'libraries'

urlpatterns = [
    path('', views.libraries, name='libraries'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Library, properties=('slug', 'name', 'address')), name='data'),

    path('libraries/<str:slug>', views.library_detail, name='library_detail'),

    path('libraries/<int:id>/edit_overdue', login_required(views.edit_overdue), name='edit_overdue'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
