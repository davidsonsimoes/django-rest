# Generated by Django 2.1.2 on 2018-10-30 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_program_horarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='program',
        ),
        migrations.AddField(
            model_name='program',
            name='horarios',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='event', to='core.Event'),
            preserve_default=False,
        ),
    ]
