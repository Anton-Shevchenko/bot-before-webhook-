# Generated by Django 3.0.2 on 2020-01-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillim', '0006_auto_20200130_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pause',
            name='start_pause',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
