from django.db import models

# Create your models here.

class Jas(models.Model):
    pass


labels = ['eichle', 'rose', 'schilte', 'schälle', 'obeabe', 'uneufe', 'miser',
    'wahl', 'slalom', '5/4']
for label in labels:
    Jas.add_to_class(label + '_1', models.IntegerField(default=0))
    Jas.add_to_class(label + '_2', models.IntegerField(default=0))

        