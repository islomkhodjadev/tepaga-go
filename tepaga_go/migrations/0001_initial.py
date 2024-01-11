# Generated by Django 5.0.1 on 2024-01-10 08:25

import tepaga_go.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
                ('img', models.ImageField(upload_to='tepaga_go/blog/')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100, validators=[tepaga_go.models.validate_phone_number])),
                ('content', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
                ('img', models.ImageField(upload_to='tepaga_go/portfolio/')),
                ('location', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('img', models.ImageField(upload_to='tepaga_go/Trips')),
                ('location', models.CharField(max_length=400)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='tepaga_go/portfolio/videos/', validators=[tepaga_go.models.validate_video_format])),
            ],
        ),
    ]