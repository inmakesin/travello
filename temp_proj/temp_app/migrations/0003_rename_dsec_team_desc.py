# Generated by Django 4.2.4 on 2023-08-21 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temp_app', '0002_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='dsec',
            new_name='desc',
        ),
    ]