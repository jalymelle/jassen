from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import JassTeam
from .forms import TeamForm, AddForm, update_AddForm

# Create your views here.
jassarten = ['Ei', 'Ro', 'Si', 'Se', 'Mi', 'Ob', 'Un', 'Sl', '4_5', 'wahl', '3_3', 'Ro12']
total = [0, 0]

def start(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            name1 = form.cleaned_data.get('name1')
            name2 = form.cleaned_data.get('name2')
            team1 = JassTeam.objects.get(qr=0)
            team2 = JassTeam.objects.get(qr=1)
            total[0], total[1] = 0, 0
            setattr(team1, 'team_name', name1)
            team1.save()
            setattr(team2, 'team_name', name2)
            team2.save()
            update_AddForm()
            print(AddForm())
            for q in range (4):
                col = JassTeam.objects.get(qr=q)
                for jassart in jassarten:
                    setattr(col, jassart, None)
                col.save()
            
            return HttpResponseRedirect(reverse('board'))
    
    else:
        form = TeamForm()

    return render(request, 'board/start.html', {'form': form})


def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            team = JassTeam.objects.get(team_name=form.cleaned_data.get('team')) 
            field = form.cleaned_data.get('jass')
            points = form.cleaned_data.get('points')
            update(team, field, points)

            return HttpResponseRedirect(reverse('board'))
    
    else:
        form = AddForm()

    return render(request, 'board/add.html', {'form': form})


def update(team, field, points):
    setattr(team, field, points)
    team.save()

    field_object = JassTeam._meta.get_field(field)
    value1 = field_object.value_from_object(JassTeam.objects.get(qr=0))
    value2 = field_object.value_from_object(JassTeam.objects.get(qr=1))
    total1 = JassTeam.objects.get(qr=2)
    total2 = JassTeam.objects.get(qr=3)
    if type(value1) == int and type(value2) == int:
        if value1 > value2:
            setattr(total1, field, (value1-value2) * (jassarten.index(field) +1) + 10)
            total1.save()
            total[0] += (value1-value2) * (jassarten.index(field) +1) + 10
        else:
            setattr(total2, field, (value2-value1) * (jassarten.index(field) +1) + 10)
            total2.save()
            total[1] += (value2-value1) * (jassarten.index(field) +1) + 10
    

def board(request):
    
    context = {
        'numbers': '1',
        'team1': JassTeam.objects.get(qr=0),
        'team2': JassTeam.objects.get(qr=1),
        'total1': JassTeam.objects.get(qr=2),
        'total2': JassTeam.objects.get(qr=3),
        'number1': total[0],
        'number2': total[1]}
        
    return render(request, 'board/board.html', context)