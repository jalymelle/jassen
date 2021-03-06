# Generated by Django 3.2.4 on 2021-06-25 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20210625_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jass_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eichle_2', models.IntegerField(default=0)),
                ('rose_2', models.IntegerField(default=0)),
                ('schilte_2', models.IntegerField(default=0)),
                ('schälle_2', models.IntegerField(default=0)),
                ('obeabe_2', models.IntegerField(default=0)),
                ('uneufe_2', models.IntegerField(default=0)),
                ('miser_2', models.IntegerField(default=0)),
                ('wahl_2', models.IntegerField(default=0)),
                ('slalom_2', models.IntegerField(default=0)),
                ('5/4_2', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='Jassarten',
            new_name='Jass_1',
        ),
        migrations.RenameField(
            model_name='jass_1',
            old_name='5/4',
            new_name='5/4_1',
        ),
        migrations.RenameField(
            model_name='jass_1',
            old_name='eichle',
            new_name='eichle_1',
        ),
        migrations.RenameField(
            model_name='jass_1',
            old_name='miser',
            new_name='miser_1',
        ),
        migrations.RenameField(
            model_name='jass_1',
            old_name='obeabe',
            new_name='obeabe_1',
        ),
        migrations.RenameField(
            model_name='jass_1',
            old_name='rose',
            new_name='rose_1',
        ),
        migrations.RenameField(
            model_name='jass_1',
            old_name='schilte',
            new_name='schilte_1',
        ),
        migrations.RenameField(
            model_name='jass_1',
            old_name='schälle',
            new_name='schälle_1',
        ),
        migrations.RenameField(
            model_name='jass_1',
            old_name='slalom',
            new_name='slalom_1',
        ),
        migrations.RenameField(
            model_name='jass_1',
            old_name='uneufe',
            new_name='uneufe_1',
        ),
        migrations.RenameField(
            model_name='jass_1',
            old_name='wahl',
            new_name='wahl_1',
        ),
    ]
