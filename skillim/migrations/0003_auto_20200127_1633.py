# Generated by Django 2.2.9 on 2020-01-27 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillim', '0002_auto_20200127_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pause',
            name='total_time',
            field=models.DurationField(blank=True, default=datetime.timedelta(0), null=True),
        ),
    ]