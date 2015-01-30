# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='deleted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
