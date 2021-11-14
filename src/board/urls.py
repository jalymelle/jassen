from .views import add, board, menu, start, end, reset, error
from django.urls import path


urlpatterns = [
    path('', menu, name='menu'),
    path('start/<int:slot>', start, name='start'),
    path('board/<int:slot>', board, name='board'),
    path('add/<int:slot>', add, name='add'),
    path('end/<int:slot>', end, name='end'),
    path('reset/<int:slot>', reset, name='reset'),
    path('error/<int:slot>/<str:message>', error, name='error')
]