# Generated by Django 2.2.5 on 2020-04-27 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy_app', '0006_auto_20200427_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='home_city',
            new_name='home_ground',
        ),
    ]