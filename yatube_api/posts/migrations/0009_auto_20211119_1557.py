# Generated by Django 2.2.16 on 2021-11-19 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20211119_1555'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_name_owner',
        ),
    ]
