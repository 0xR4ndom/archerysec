# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-09 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staticscanners", "0006_findbugs_scan_results_db_priority"),
    ]

    operations = [
        migrations.AddField(
            model_name="findbugs_scan_results_db",
            name="risk",
            field=models.TextField(blank=True),
        ),
    ]
