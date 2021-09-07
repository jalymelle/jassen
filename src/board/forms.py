from django import forms
from .models import JassTeam, all_fields, codes


class TeamForm(forms.Form):
    name1 = forms.CharField(label='Name Team 1', max_length=10)
    name2 = forms.CharField(label='Name Team 2', max_length=10)
    length = forms.IntegerField(label='Anzahl Tafeln', max_value=3)


jassarten = []
for jassart in all_fields[0:9]:
    option = (jassart, codes[jassart[:-2]] + ' ' + jassart[-1])
    jassarten.append(option)

for jassart in all_fields[9:]:
    option = (jassart, codes[jassart[:-3]] + ' ' + jassart[-2:])
    jassarten.append(option)
        

teams = []

def update_AddForm():
    team1 = JassTeam.objects.get(qr=0)
    team2 = JassTeam.objects.get(qr=1)
    teams.append((team1.team_name, team1.team_name))
    teams.append((team2.team_name, team2.team_name))



class AddForm1(forms.Form):
    team = forms.ModelChoiceField(label='Team', queryset=JassTeam.objects.all())
    jass = forms.CharField(label='Jass', widget=forms.Select(choices=jassarten[0:12]))
    points = forms.IntegerField(label='Punkte', min_value=0, max_value=16)
    match = forms.BooleanField(label='Match', required=False)


class AddForm2(forms.Form):
    team = forms.ModelChoiceField(label='Team', queryset=JassTeam.objects.all())
    jass = forms.CharField(label='Jass', widget=forms.Select(choices=jassarten[0:24]))
    points = forms.IntegerField(label='Punkte', min_value=0, max_value=16)
    match = forms.BooleanField(label='Match', required=False)


class AddForm3(forms.Form):
    team = forms.ModelChoiceField(label='Team', queryset=JassTeam.objects.all())
    jass = forms.CharField(label='Jass', widget=forms.Select(choices=jassarten))
    points = forms.IntegerField(label='Punkte', min_value=0, max_value=16)
    match = forms.BooleanField(label='Match', required=False)


    






