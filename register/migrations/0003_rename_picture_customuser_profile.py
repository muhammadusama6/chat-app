# Generated by Django 4.2 on 2023-04-11 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_customuser_delete_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='picture',
            new_name='profile',
        ),
    ]
