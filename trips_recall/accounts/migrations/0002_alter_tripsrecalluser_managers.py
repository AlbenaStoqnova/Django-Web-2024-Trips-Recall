# Generated by Django 5.0.3 on 2024-03-25 09:35

import trips_recall.accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='tripsrecalluser',
            managers=[
                ('objects', trips_recall.accounts.models.TripsRecallUserManager()),
            ],
        ),
    ]