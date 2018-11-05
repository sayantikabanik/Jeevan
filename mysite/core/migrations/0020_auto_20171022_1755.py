# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-22 12:25
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20171022_1454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productdb',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='productdb',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, keep_meta=True, quality=0, size=[300, 300], upload_to='products/%Y/%m/%d'),
        ),
    ]
