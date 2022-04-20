# Generated by Django 4.0.4 on 2022-04-19 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_teammembers_team_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='team_lead',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
