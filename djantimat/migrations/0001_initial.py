# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slang',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(unique=True, max_length=64, verbose_name='\u041d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0430 \u043c\u0430\u0442\u0435\u0440\u043d\u043e\u0433\u043e \u0441\u043b\u043e\u0432\u0430')),
            ],
            options={
                'verbose_name': '\u041c\u0430\u0442\u0435\u0440\u043d\u043e\u0435 \u0441\u043b\u043e\u0432\u043e',
                'verbose_name_plural': '\u041c\u0430\u0442\u0435\u0440\u043d\u044b\u0435 \u0441\u043b\u043e\u0432\u0430',
            },
            bases=(models.Model,),
        ),
    ]
