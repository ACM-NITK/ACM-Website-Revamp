# Generated by Django 2.0 on 2021-03-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acm', '0012_auto_20200811_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='year',
            field=models.IntegerField(default=2019),
            preserve_default=False,
        ),
    ]
