# Generated by Django 5.0.3 on 2024-03-24 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('pet_photo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='photos.tripphoto')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_photo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='photos.tripphoto')),
            ],
        ),
    ]
