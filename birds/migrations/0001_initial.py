# Generated by Django 3.0.8 on 2020-07-21 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=250)),
                ('scientific_name', models.CharField(max_length=250)),
            ],
        ),
    ]
