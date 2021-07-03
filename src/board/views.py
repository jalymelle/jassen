from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import JassTeam
from .forms import TeamForm

# Create your views here.
def start(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            # JassTeam.objects.all().delete()
            return HttpResponseRedirect(reverse('board') )
    
    else:
        form = TeamForm()

    return render(request, 'board/start.html', {'form': form})


def add(request):
    return render(request, 'board/add.html', {})


def board(request):
    team1 = JassTeam.objects.get(id=1)
    team2 = JassTeam.objects.get(id=2)
    
    context = {
        'numbers': '1', 
        'team1': team1,
        'team2': team2}
        
    return render(request, 'board/board.html', context)