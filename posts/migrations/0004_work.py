# Generated by Django 3.2.9 on 2022-01-29 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20211228_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('subheading', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-from_date'],
            },
        ),
    ]
