# Generated by Django 3.1.4 on 2021-01-13 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20210113_2253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='notfication_type',
            new_name='notification_type',
        ),
    ]