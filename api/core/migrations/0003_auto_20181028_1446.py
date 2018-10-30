# Generated by Django 2.1.2 on 2018-10-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181028_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='canal',
            new_name='frequencia',
        ),
        migrations.AddField(
            model_name='channel',
            name='faixa_freq',
            field=models.CharField(choices=[('FM', 'Frequancia FM'), ('AM', 'Frequencia AM')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]