# Generated by Django 3.2.4 on 2021-09-03 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0016_auto_20210828_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='designation',
        ),
    ]
