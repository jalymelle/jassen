# Generated by Django 3.2.4 on 2021-10-08 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0028_auto_20210904_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jassteam',
            name='team_name',
            field=models.CharField(max_length=8),
        ),
    ]