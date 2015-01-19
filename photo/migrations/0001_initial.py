# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dir_name', models.CharField(max_length=128)),
                ('display_name', models.CharField(max_length=128)),
                ('summary', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
