# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 18:38
from __future__ import unicode_literals

import audio_transcoder.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('mp3_file', models.FileField(upload_to='')),
                ('ogg_file', models.FileField(blank=True, upload_to=audio_transcoder.models.md5_directory_path)),
                ('wav_file', models.FileField(blank=True, upload_to=audio_transcoder.models.md5_directory_path)),
                ('ac3_file', models.FileField(blank=True, upload_to=audio_transcoder.models.md5_directory_path)),
            ],
        ),
    ]
