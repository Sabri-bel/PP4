# Generated by Django 4.2.19 on 2025-02-13 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_reservationrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='is_staff',
        ),
    ]
