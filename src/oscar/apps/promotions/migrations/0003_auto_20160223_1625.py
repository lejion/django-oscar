# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.sites.managers


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('promotions', '0002_auto_20151028_2105'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='pagepromotion',
            managers=[
                ('objects', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AddField(
            model_name='pagepromotion',
            name='sites',
            field=models.ManyToManyField(to='sites.Site'),
        ),
    ]
