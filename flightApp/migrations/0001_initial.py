# Generated by Django 4.0.6 on 2022-08-09 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flightNumber', models.CharField(max_length=10)),
                ('operatinAirLines', models.CharField(max_length=20)),
                ('departureCity', models.CharField(max_length=20)),
                ('arrivalCity', models.CharField(max_length=20)),
                ('departure', models.DateField()),
                ('estimatedTimeDepature', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fligth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flightApp.flight')),
                ('passenger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flightApp.passenger')),
            ],
        ),
    ]
