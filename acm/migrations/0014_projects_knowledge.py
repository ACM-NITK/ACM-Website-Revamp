# Generated by Django 2.2 on 2021-03-27 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acm', '0013_projects_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='knowledge',
            field=models.TextField(blank=True),
        ),
    ]