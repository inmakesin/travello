# Generated by Django 4.2.4 on 2023-09-27 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp_app', '0003_rename_dsec_team_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='year',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='img',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
