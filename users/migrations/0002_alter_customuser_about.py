# Generated by Django 3.2.9 on 2021-11-26 23:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='about',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(300, message='Please enter more text')]),
        ),
    ]
