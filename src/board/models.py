from django.db import models

# Create your models here.
class JassTeam(models.Model):
    team_name = models.CharField(max_length=20, null=False)
    qr = models.IntegerField(null=False, unique=True)


labels = ['Ei', 'Ro', 'Si', 'Se', 'Mi', 'Ob', 'Un', 'Sl', '4_5', 'wahl', '3_3', 'Ro12']
for label in labels:
    JassTeam.add_to_class(label, models.IntegerField(null=True, blank=True, default=None))
