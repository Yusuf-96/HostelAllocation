# Generated by Django 3.0.7 on 2020-08-26 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200826_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('mr', 'MALE'), ('mrs', 'FEMALE')], max_length=10),
        ),
    ]
