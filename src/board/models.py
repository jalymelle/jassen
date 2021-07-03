from django.db import models

# Create your models here.
class JassTeam(models.Model):
    team_name = models.CharField(max_length=20, null=False, unique=True)


labels = ['Ei', 'Ro', 'Si', 'Se', 'Mi', 'Ob', 'Un', 'Sl', '4/5', '?', '3/3', 'Ro12']
for label in labels:
    JassTeam.add_to_class(label, models.IntegerField(default=0))



        