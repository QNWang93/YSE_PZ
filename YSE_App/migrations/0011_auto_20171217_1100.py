# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-17 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('YSE_App', '0010_transientphotdata_discovery_point'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hostfollowup',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='hostobservationtask',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='transientfollowup',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='transientobservationtask',
            options={'ordering': ['-id']},
        ),
    ]
