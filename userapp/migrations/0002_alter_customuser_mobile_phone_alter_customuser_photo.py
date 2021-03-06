# Generated by Django 4.0.4 on 2022-04-18 11:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mobile_phone',
            field=models.CharField(default=9090908821, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid international mobile phone number starting with +(country code)', regex='^\\+(?:[0-9]●?){6,14}[0-9]$')], verbose_name='Mobile phone'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(upload_to='pics', verbose_name='Photo'),
        ),
    ]
