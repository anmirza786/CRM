# Generated by Django 4.2.2 on 2023-06-13 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_date_authcode_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='authcode',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 13, 18, 49, 52, 765264)),
        ),
    ]