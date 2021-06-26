from .views import board
from django.urls import path


urlpatterns = [
    path('', board, ),
]