# Generated by Django 3.0.7 on 2020-07-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_auto_20200719_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
    ]
