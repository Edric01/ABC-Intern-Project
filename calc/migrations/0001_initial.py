# Generated by Django 3.2.4 on 2021-06-14 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
    ]
