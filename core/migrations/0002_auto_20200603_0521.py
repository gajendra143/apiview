# Generated by Django 2.2 on 2020-06-03 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='id_name',
            field=models.IntegerField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='real_name',
            field=models.CharField(max_length=1000),
        ),
    ]
