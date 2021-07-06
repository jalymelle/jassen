from django import forms
from .models import JassTeam

class TeamForm(forms.Form):
    name1 = forms.CharField(label='Name Team 1', max_length=10)
    name2 = forms.CharField(label='Name Team 2', max_length=10)

jassarten = [
    ('Ei', 'Ei'),
    ('Ro', 'Ro'),
    ('Si', 'Si'),
    ('Se', 'Se'),
    ('Mi', 'Mi'),
    ('Ob', '↓'),
    ('Un', '↑'),
    ('Sl', '☇'),
    ('4_5', '4/5'),
    ('wahl', '?'),
    ('3_3', '3/3'),
    ('Ro12', 'Ro'),
]

teams = []

def update_AddForm():
    team1 = JassTeam.objects.get(qr=0)
    team2 = JassTeam.objects.get(qr=1)
    teams.append((team1.team_name, team1.team_name))
    teams.append((team2.team_name, team2.team_name))



class AddForm(forms.Form):
    team = forms.ModelChoiceField(label='Team', queryset=JassTeam.objects.all())
    jass = forms.CharField(label='Jass', widget=forms.Select(choices=jassarten))
    points = forms.IntegerField(label='Punkte', min_value=0, max_value=16)
    match = forms.BooleanField(label='Match', required=False)


