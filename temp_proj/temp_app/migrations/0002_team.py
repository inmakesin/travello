# Generated by Django 4.2.4 on 2023-08-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=250)),
                ('dsec', models.TextField()),
            ],
        ),
    ]
