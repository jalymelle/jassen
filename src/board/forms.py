from django import forms
from .models import JassTeam


class TeamForm(forms.Form):
    name1 = forms.CharField(label='Name Team 1', max_length=10)
    name2 = forms.CharField(label='Name Team 2', max_length=10)
    length = forms.IntegerField(label='Anzahl Tafeln', max_value=3)


jassarten = []


class AddForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.qr1 = kwargs.pop('qr1')
        self.qr2 = kwargs.pop('qr2')
        self.jasse = kwargs.pop('jasse')
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields['team'].queryset =  JassTeam.objects.filter(qr=self.qr1) | JassTeam.objects.filter(qr=self.qr2)
        self.fields['jass'].widget = forms.Select(choices=self.jasse)

    class Meta:
        model = JassTeam
        fields = ['team', 'jass', 'points', 'macht']
    
    team = forms.ModelChoiceField(label='Team', queryset=None)
    jass = forms.CharField(label='Jass', widget=forms.Select(choices=jassarten))
    points = forms.IntegerField(label='Punkte', min_value=0, max_value=16)
    match = forms.BooleanField(label='Match', required=False)


    






