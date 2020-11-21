# pages/urls.py

from django.urls import path
from .views import StartPage

urlpatterns = [
    path('', StartPage.as_view(), name='home')
]
