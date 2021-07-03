from .views import start, board, add
from django.urls import path


urlpatterns = [
    path('', start, name='start'),
    path('board/', board, name='board'),
    path('add/', add, name='add')
]