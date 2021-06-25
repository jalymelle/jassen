from django.db import models

# Create your models here.

class Jassarten(models.Model):
    types = ['eichle', 'rose', 'schilte', 'schälle', 'obeabe', 'uneufe', 'miser',
    'wahl', 'slalom', '5/4']
    for t in types:
        t = models.IntegerField(name=t, max_length=2)
        
        