# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msalamaclient', '0005_auto_20150507_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstchoicedate', models.DateTimeField()),
                ('secondchoicedate', models.DateTimeField()),
                ('purposeofvisit', models.CharField(max_length=600)),
            ],
        ),
    ]
