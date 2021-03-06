from django.db import models

# Create your models here.
class JassTeam(models.Model):
    team_name = models.CharField(max_length=8, null=False)
    qr = models.IntegerField(null=False, unique=True)

    def __str__(self):
        return f'{self.team_name}'

labels = ('Ei', 'Ro', 'Si', 'Se', 'Mi', 'Ob', 'Un', 'Sl', '4_5', 'wahl', '3_3', 'Ro12')
all_fields = []
codes = {
    'Ei' : 'Ei',
    'Ro' : 'Ro',
    'Si' : 'Si',
    'Se' : 'Se',
    'Mi' : 'Mi',
    'Ob' : '↓',
    'Un' : '↑',
    'Sl' : '☇',
    '4_5' : '4/5',
    'wahl' : '?',
    '3_3' : '3/3',
    'Ro12' : 'Ro*',
}

# times number
j = 0

for label in labels*3:
    j += 1
    JassTeam.add_to_class(label + '_' + str(j), models.IntegerField(null=True, blank=True, default=None))
    all_fields.append(label + '_' + str(j))