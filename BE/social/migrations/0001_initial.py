# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 15:11
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=50)),
                ('profession', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_image', models.URLField(blank=True, max_length=1024, null=True)),
                ('profile_cover', models.URLField(blank=True, max_length=1024, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('followed', models.ManyToManyField(related_name='_user_followed_+', to='social.User')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
