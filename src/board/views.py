from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import JassTeam, all_fields, codes
from .forms import TeamForm, AddForm 

# Create your views here.
jassarten = []
total = [0, 0]

def start(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            name1 = form.cleaned_data.get('name1')
            name2 = form.cleaned_data.get('name2')
            number = form.cleaned_data.get('length')
            for i in all_fields[0:number*12]:
                jassarten.append(i)

            team1 = JassTeam.objects.get(qr=0)
            team2 = JassTeam.objects.get(qr=1)
            total[0], total[1] = 0, 0
            setattr(team1, 'team_name', name1)
            team1.save()
            setattr(team2, 'team_name', name2)
            team2.save()
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
            match = form.cleaned_data.get('match')
            update(team, field, points, match)

            return HttpResponseRedirect(reverse('board'))
    
    else:
        form = AddForm()

    return render(request, 'board/add.html', {'form': form})


def update(team, field, points, match):
    if match: 
        setattr(team, field, 17)
    else:
        setattr(team, field, points)
    team.save()

    field_object = JassTeam._meta.get_field(field)
    value1 = field_object.value_from_object(JassTeam.objects.get(qr=0))
    value2 = field_object.value_from_object(JassTeam.objects.get(qr=1))
    total1 = JassTeam.objects.get(qr=2)
    total2 = JassTeam.objects.get(qr=3)
    if type(value1) == int and type(value2) == int:
        if value1 > value2:
            if value1 == 17:
                setattr(total1, field, (16-value2) * (jassarten.index(field) +1) + 20)
            else:
                setattr(total1, field, (value1-value2) * (jassarten.index(field) +1) + 10)
            setattr(total2, field, None)
        elif value2 > value1:
            if value2 == 17:
                setattr(total2, field, (16-value1) * (jassarten.index(field) +1) + 20)
            else:
                setattr(total2, field, (value2-value1) * (jassarten.index(field) +1) + 10)
            setattr(total1, field, None)
        
        else:
            setattr(total1, field, None)
            setattr(total2, field, None)

        total1.save()
        total2.save()
        total[0], total[1] = 0, 0
        for jassart in jassarten:
            t1 = getattr(total1, jassart)
            t2 = getattr(total2, jassart)
            if t1 != None:
                total[0] += t1
            if t2 != None:
                total[1] += t2

    

def board(request):
    data = []
    for field in jassarten:
        data_row = []
        data_row.append(codes[field[:-2]] + ' ' + field[-1])
        for i in range(4):
            data_row.append(getattr(JassTeam.objects.get(qr=i), field))
        data.append(data_row)

    context = {
        'team1': JassTeam.objects.get(qr=0),
        'team2': JassTeam.objects.get(qr=1),
        'number1': total[0],
        'number2': total[1],
        'data': data}
        
    return render(request, 'board/board.html', context)