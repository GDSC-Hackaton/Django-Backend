# Generated by Django 5.0.3 on 2024-04-03 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_address_block_alter_address_office_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='hosts',
        ),
    ]
