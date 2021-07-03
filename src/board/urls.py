from .views import board, start, add
from django.urls import path


urlpatterns = [
    path('', start, name='start'),
    path('board/', board, name='board'),
    path('add/', add, name='add')
]