# Generated by Django 3.2.4 on 2021-07-03 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0014_auto_20210703_0943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jassteam',
            old_name='wahl4_5',
            new_name='4_5',
        ),
        migrations.AddField(
            model_name='jassteam',
            name='wahl',
            field=models.IntegerField(default=0),
        ),
    ]
