from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import JassTeam, all_fields, codes
from .forms import TeamForm, AddForm1, AddForm2, AddForm3

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
    print(context)

    return render(request, 'board/menu.html', context)


def start(request, slot):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            name1 = form.cleaned_data.get('name1')
            name2 = form.cleaned_data.get('name2')
            number[slot] = form.cleaned_data.get('length')
            for j in all_fields[0:number[0]*12]:
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
    for i in jassarten[slot]:
        jassarten.remove(i)
    
    return render(request, 'board/menu.html', {})


def add(request):
    if request.method == 'POST':
        if number[0] == 1:
            form = AddForm1(request.POST)
        elif number[0] == 2:
            form = AddForm2(request.POST)
        else:
            form = AddForm3(request.POST)
        if form.is_valid():
            team = JassTeam.objects.get(team_name=form.cleaned_data.get('team')) 
            field = form.cleaned_data.get('jass')
            points = form.cleaned_data.get('points')
            match = form.cleaned_data.get('match')
            update(team, field, points, match)

            return HttpResponseRedirect(reverse('board'))
    
    else:
        if number[0] == 1:
            form = AddForm1()
        elif number[0] == 2:
            form = AddForm2()
        else:
            form = AddForm3()

    return render(request, 'board/add.html', {'form': form})
    

def board(request, slot):
    print('here')
    data = []
    if len(jassarten[slot]) == 0:
        return HttpResponseRedirect(reverse('start', kwargs={'slot': slot}))
    else: 
        for field in jassarten[slot]:
            data_row = []
            if jassarten[slot].index(field) < 9:
                data_row.append(codes[field[:-2]] + ' ' + field[-1])
            else: 
                data_row.append(codes[field[:-3]] + ' ' + ' ' + field[-2:])
            for i in range(4):
                data_row.append(getattr(JassTeam.objects.get(qr= 4 * slot + i), field))
            data.append(data_row)
        
        total_0 = 0
        total_1 = 0
        
        if total[0] > total[1]:
            total_0 = total[0] - total[1]
    
        elif total[0] > total[1]:
            total_1 = total[1] - total[0]
        

        # difference instead of two totals, finish button, continue button
        context = {
            'team1': JassTeam.objects.get(qr= 4 * slot + 1),
            'team2': JassTeam.objects.get(qr= 4 * slot + 2),
            'number1': total_0,
            'number2': total_1,
            'data': data}
            
        return render(request, 'board/board.html', context)


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