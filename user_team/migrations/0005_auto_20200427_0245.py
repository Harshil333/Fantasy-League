# Generated by Django 2.2.5 on 2020-04-26 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_team', '0004_userteam_total_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userplayer',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fantasy_app.Player'),
        ),
    ]