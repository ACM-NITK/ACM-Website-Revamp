# Generated by Django 2.2.6 on 2019-12-10 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acm', '0002_auto_20191209_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sig',
            name='smp_head_contact_number',
        ),
        migrations.RemoveField(
            model_name='sig',
            name='smp_head_name',
        ),
    ]