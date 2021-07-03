from django import forms

class TeamForm(forms.Form):
    name1 = forms.CharField(label='Name Team 1', max_length=10)
    name2 = forms.CharField(label='Name Team 2', max_length=10)