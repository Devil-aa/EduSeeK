# Generated by Django 3.2 on 2021-09-01 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('vacancy', models.CharField(max_length=255)),
                ('deadline', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
                ('stipend', models.CharField(max_length=255)),
                ('skills', models.CharField(max_length=255)),
                ('last_date', models.CharField(max_length=255)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intern', to='intership.location')),
            ],
        ),
    ]