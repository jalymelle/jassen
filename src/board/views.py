from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import JassTeam, all_fields, codes
from .forms import TeamForm, AddForm

# Create your views here.
jassarten = [[], [], [], []]
total = [[0, 0], [0, 0], [0, 0], [0, 0]]
number = [0, 0, 0, 0]


def menu(request):
    board_names = ['board_0', 'board_1', 'board_2', 'board_3']
    context = {
    }
    for i in range(4):
        if len(jassarten[i]) != 0:
            team_name = JassTeam.objects.get(qr=4*i + 1).team_name + ' & ' + JassTeam.objects.get(qr=4*i + 2).team_name
            context[board_names[i]] = team_name
        else:
            context[board_names[i]] = 'Leer'

    return render(request, 'board/menu.html', context)


def start(request, slot):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            name1 = form.cleaned_data.get('name1')
            name2 = form.cleaned_data.get('name2')
            number[slot] = form.cleaned_data.get('length')
            for j in all_fields[0:number[slot]*12]:
                jassarten[slot].append(j)

            team1 = JassTeam.objects.get(qr=4*slot + 1)
            team2 = JassTeam.objects.get(qr=4*slot + 2)
            total[slot][0], total[slot][1] = 0, 0
            setattr(team1, 'team_name', name1)
            team1.save()
            setattr(team2, 'team_name', name2)
            team2.save()
            for q in range (4):
                col = JassTeam.objects.get(qr=4*slot + 1 + q)
                for jassart in jassarten[slot]:
                    setattr(col, jassart, None)
                col.save()
            return HttpResponseRedirect(reverse('board', kwargs={'slot': slot}))
    
    else:
        form = TeamForm()

    return render(request, 'board/start.html', {'form': form, 'slot':slot})


def end(request, slot):
    jassarten[slot] = []
    
    return HttpResponseRedirect(reverse('menu'))


def add(request, slot):
    if request.method == 'POST':
        form = AddForm(request.POST, qr1=4 * slot + 1, qr2=4 * slot + 2, jasse=[])
        if form.is_valid():
            team = form.cleaned_data.get('team')
            field = form.cleaned_data.get('jass')
            points = form.cleaned_data.get('points')
            match = form.cleaned_data.get('match')
            update(team, field, points, match, slot)

            return HttpResponseRedirect(reverse('board', kwargs={'slot': slot}))
    
    else:
        jasse = []
        for jassart in jassarten[slot]:
            if jassarten[slot].index(jassart) < 9:
                jasse.append((jassart, codes[jassart[:-2]] + ' ' + jassart[-1]))
            else: 
                jasse.append((jassart, codes[jassart[:-3]] + ' ' + jassart[-2:]))
            
        form = AddForm(qr1=4 * slot + 1, qr2=4 * slot + 2, jasse=jasse)


    context = {'form': form, 'slot': slot}
    return render(request, 'board/add.html', context)
    

def board(request, slot):
    if len(jassarten[slot]) == 0:
        return HttpResponseRedirect(reverse('start', kwargs={'slot': slot}))

    data = []
    for field in jassarten[slot]:
        data_row = []
        if jassarten[slot].index(field) < 9:
            data_row.append(codes[field[:-2]] + ' ' + field[-1])
        else: 
            data_row.append(codes[field[:-3]] + ' ' + ' ' + field[-2:])
        for i in range(4):
            data_row.append(getattr(JassTeam.objects.get(qr= 4 * slot + 1 + i), field))
        data.append(data_row)
    
    total_0 = 0
    total_1 = 0
    
    if total[slot][0] > total[slot][1]:
        total_0 = total[slot][0] - total[slot][1]

    elif total[slot][0] > total[slot][1]:
        total_1 = total[slot][1] - total[slot][0]
    

    context = {
        'team1': JassTeam.objects.get(qr= 4 * slot + 1),
        'team2': JassTeam.objects.get(qr= 4 * slot + 2),
        'number1': total_0,
        'number2': total_1,
        'data': data,
        'slot': slot}
            
    return render(request, 'board/board.html', context)


def update(team, field, points, match, slot):
    if match: 
        setattr(team, field, 17)
    else:
        setattr(team, field, points)
    team.save()


    field_object = JassTeam._meta.get_field(field)
    value1 = field_object.value_from_object(JassTeam.objects.get(qr=4* slot + 1))
    value2 = field_object.value_from_object(JassTeam.objects.get(qr=4* slot + 2))
    total1 = JassTeam.objects.get(qr=4* slot + 3)
    total2 = JassTeam.objects.get(qr=4* slot + 4)
    if type(value1) == int and type(value2) == int:
        if value1 > value2:
            if value1 == 17:
                setattr(total1, field, (16-value2) * (jassarten[slot].index(field) +1) + 20)
            else:
                setattr(total1, field, (value1-value2) * (jassarten[slot].index(field) +1) + 10)
            setattr(total2, field, None)
        elif value2 > value1:
            if value2 == 17:
                setattr(total2, field, (16-value1) * (jassarten[slot].index(field) +1) + 20)
            else:
                setattr(total2, field, (value2-value1) * (jassarten[slot].index(field) +1) + 10)
            setattr(total1, field, None)
        
        else:
            setattr(total1, field, None)
            setattr(total2, field, None)
        total1.save()
        total2.save()
        total[slot][0], total[slot][1] = 0, 0
        for jassart in jassarten[slot]:
            t1 = getattr(total1, jassart)
            t2 = getattr(total2, jassart)
            if t1 != None:
                total[slot][0] += t1
            if t2 != None:
                total[slot][1] += t2
        