# Generated by Django 4.0.4 on 2022-06-03 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='created_at',
            new_name='date',
        ),
    ]