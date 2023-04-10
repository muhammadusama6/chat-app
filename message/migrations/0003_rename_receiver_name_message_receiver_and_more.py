# Generated by Django 4.2 on 2023-04-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_message_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='receiver_name',
            new_name='receiver',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='sender_name',
            new_name='sender',
        ),
        migrations.AddField(
            model_name='message',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]