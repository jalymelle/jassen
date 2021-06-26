from django.db import models

# Create your models here.

class Jas(models.Model):
    team_name = models.CharField(max_length=20, null=False, unique=True)


labels = ['eichle', 'rose', 'schilte', 'schälle', 'obeabe', 'uneufe', 'miser',
    'wahl', 'slalom', '5/4']
for label in labels:
    Jas.add_to_class(label, models.IntegerField(default=0))

        