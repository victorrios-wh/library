# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_auto_20250326_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='portadas/'),
        ),
    ]
