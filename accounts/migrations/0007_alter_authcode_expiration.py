# Generated by Django 4.2.2 on 2023-06-13 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_authcode_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authcode',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 13, 18, 50, 25, 24584)),
        ),
    ]