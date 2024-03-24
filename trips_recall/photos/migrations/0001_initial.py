# Generated by Django 5.0.3 on 2024-03-24 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/')),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('trips', models.ManyToManyField(to='trips.trip')),
            ],
        ),
    ]