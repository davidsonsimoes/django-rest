# Generated by Django 2.1.2 on 2018-10-28 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='canal',
            field=models.CharField(max_length=10),
        ),
    ]
