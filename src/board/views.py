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
    
    
    context = {
        'numbers': '1', 
        'team1': team1,
        'team2': team2}
        
    return render(request, 'board/board.html', context)