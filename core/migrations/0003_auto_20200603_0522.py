# Generated by Django 2.2 on 2020-06-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200603_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='id_name',
            field=models.IntegerField(unique=True),
        ),
    ]