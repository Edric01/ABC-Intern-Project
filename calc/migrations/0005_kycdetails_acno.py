# Generated by Django 3.2.4 on 2021-07-14 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_kycdetails_verify'),
    ]

    operations = [
        migrations.AddField(
            model_name='kycdetails',
            name='acno',
            field=models.CharField(default=0, max_length=14),
            preserve_default=False,
        ),
    ]