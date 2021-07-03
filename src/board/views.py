from django.shortcuts import render
from .models import JassTeam

# Create your views here.
#def start(request):
    #return render(request, 'board/start.html', {})

#def start(request):
    #return render('board/start.html', {'output': output})


def start(request):
    model = JassTeam
    field_names = [f.name for f in model._meta.get_fields()]
    data = [[getattr(ins, name) for name in field_names]
            for ins in JassTeam.objects.prefetch_related().all()]
    return render(request, 'board/start.html', {'field_names': field_names, 'data': data})


def board(request):
    team1 = JassTeam.objects.get(id=1)
    team2 = JassTeam.objects.get(id=2)

    fields = JassTeam._meta.get_fields()
    fields = fields[1:]
    names = [field.name for field in fields]
    fields_1 = []
    fields_2 = []

    for name in names:
        field_object = JassTeam._meta.get_field(name)
        fields_1.append(field_object.value_from_object(team1))
        fields_2.append(field_object.value_from_object(team2))
    
    
    context = {
        'names': names, 
        'team1': fields_1,
        'team2': team2}
        
    return render(request, 'board/board.html', context)