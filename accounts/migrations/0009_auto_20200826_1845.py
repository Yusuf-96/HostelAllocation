# Generated by Django 3.0.7 on 2020-08-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200826_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('male', 'Mr'), ('female', 'Mrs')], max_length=10),
        ),
    ]
