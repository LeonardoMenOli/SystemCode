# Generated by Django 2.2.7 on 2020-06-27 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='fecha',
            field=models.CharField(max_length=20),
        ),
    ]