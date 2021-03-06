# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-26 01:20
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations
from YSE_App.models.transient_models import *

def migrate_data_forward(apps, schema_editor):
    for instance in Transient.objects.all():
        print("Generating slug for %s"%instance)
        instance.save() # Will trigger slug update

def migrate_data_backward(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('YSE_App', '0013_remove_transient_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='transient',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True),
			preserve_default=False,
        ),
		migrations.RunPython(
			migrate_data_forward,
			migrate_data_backward,
			),
    ]
