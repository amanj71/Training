# Generated by Django 4.2.4 on 2023-09-01 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Name', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='realese_year',
            field=models.IntegerField(),
        ),
    ]
