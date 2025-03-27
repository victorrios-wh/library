# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_auto_20250325_1823'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='editor',
            options={'verbose_name_plural': 'Editores', 'ordering': ['nombre']},
        ),
    ]
