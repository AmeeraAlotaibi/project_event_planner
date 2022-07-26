# Generated by Django 4.0.6 on 2022-07-24 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizer', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=300)),
                ('num_of_seats', models.PositiveIntegerField()),
                ('booked_seats', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]
