# Generated by Django 3.2.9 on 2021-11-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rating_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
