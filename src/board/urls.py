from .views import board, start
from django.urls import path


urlpatterns = [
    path('', start),
    path('board/', board)
]