from django.shortcuts import render
from .models import JassTeam

# Create your views here.
def start(request):
    return render(request, 'board/start.html', {})


def board(request):
    Jassarten = JassTeam.objects.all()
    print(Jassarten)
    return render(request, 'board/board.html', {'Jassarten': Jassarten})