from django.shortcuts import render
from .models import Jas

# Create your views here.
def board(request):
    Jassarten = Jas.objects.all()
    print(Jassarten)
    return render(request, 'board/board.html', {'Jassarten': Jassarten})