from .views import add, board, menu, start, end
from django.urls import path


urlpatterns = [
    path('', menu, name='menu'),
    path('start/<int:slot>', start, name='start'),
    path('board/<int:slot>', board, name='board'),
    path('add/', add, name='add'),
    path('end/', end, name='end')
]