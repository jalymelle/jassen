from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import JassTeam
from .forms import TeamForm, AddForm

# Create your views here.
def start(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            JassTeam.objects.all().delete()
            name1 = form.cleaned_data.get('name1')
            name2 = form.cleaned_data.get('name2')
            cols = [name1, name2, 'total1', 'total2']
            for col in cols:
                JassTeam.objects.create(team_name=col)
            
            return HttpResponseRedirect(reverse('board'), {'form': form})
    
    else:
        form = TeamForm()
        print('here')

    return render(request, 'board/start.html', )


def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            team = JassTeam.objects.get(team_name=form.cleaned_data.get('team')) 
            field = form.cleaned_data.get('jass')
            points = form.cleaned_data.get('points')
            update(team, field, points)
            
            return HttpResponseRedirect(reverse('board') )
    
    else:
        form = AddForm()

    return render(request, 'board/add.html', {'form': form})

def update(team, field, points):
    setattr(team, field, points)
    team.save()


def board(request):
    print(JassTeam.objects.all())
    team1 = JassTeam.objects.get(id=1)
    team2 = JassTeam.objects.get(id=2)
    
    context = {
        'numbers': '1',
        'team1': team1,
        'team2': team2}
        
    return render(request, 'board/board.html', context)