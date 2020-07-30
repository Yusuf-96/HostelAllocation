# Generated by Django 3.0.7 on 2020-07-27 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_room_is_taken'),
        ('allocate', '0002_auto_20200721_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocate',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allocate', to='room.Room', unique=True),
        ),
    ]
