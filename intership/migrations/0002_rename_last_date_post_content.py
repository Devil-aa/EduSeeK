# Generated by Django 3.2.6 on 2021-09-01 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intership', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='last_date',
            new_name='content',
        ),
    ]
