# Generated by Django 2.2.9 on 2020-01-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillim', '0007_auto_20200130_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='current_status',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]
