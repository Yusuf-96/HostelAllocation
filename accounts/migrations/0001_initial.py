# Generated by Django 3.0.7 on 2020-07-27 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('status', models.CharField(default='Active', max_length=10)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('profile', models.ImageField(blank=True, default='images/users/default/brand.png', null=True, upload_to='images/users')),
            ],
        ),
    ]
