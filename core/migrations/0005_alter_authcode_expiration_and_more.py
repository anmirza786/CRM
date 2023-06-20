# Generated by Django 4.2.2 on 2023-06-20 13:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_authcode_expiration_passwordresettoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authcode',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 20, 15, 40, 31, 744905)),
        ),
        migrations.AlterField(
            model_name='passwordresettoken',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
