# Generated by Django 2.1.2 on 2018-10-28 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20181028_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='program',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='program', to='core.Program'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='program',
            name='horarios',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='core.Event'),
        ),
    ]
