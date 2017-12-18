# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Again',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('prolific_id', models.CharField(max_length=50, default='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ip_address', models.CharField(max_length=120, default='')),
                ('asn', models.CharField(max_length=10, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Failed',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ip_address', models.CharField(max_length=120, default='')),
                ('asn', models.CharField(max_length=10, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('prolific_id', models.CharField(max_length=50, default='')),
                ('spoofer_URL', models.CharField(max_length=70, default='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ip_address', models.CharField(max_length=120, default='')),
                ('asn', models.CharField(max_length=10, default='')),
            ],
        ),
    ]
