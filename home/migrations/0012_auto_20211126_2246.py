# Generated by Django 3.2.9 on 2021-11-26 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20211126_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='username',
        ),
        migrations.RemoveField(
            model_name='review',
            name='username',
        ),
    ]
