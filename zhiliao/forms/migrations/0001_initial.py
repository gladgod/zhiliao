# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import zhiliao.core.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', zhiliao.core.fields.OrderField(null=True, verbose_name='Order')),
                ('label', models.CharField(max_length=200, verbose_name='Label')),
                ('field_type', models.IntegerField(verbose_name='Type', choices=[(1, 'Single line text'), (2, 'Multi line text'), (3, 'Email'), (13, 'Number'), (14, 'URL'), (4, 'Check box'), (5, 'Check boxes'), (6, 'Drop down'), (7, 'Multi select'), (8, 'Radio buttons'), (9, 'File upload'), (10, 'Date'), (11, 'Date/time'), (15, 'Date of birth'), (12, 'Hidden')])),
                ('required', models.BooleanField(default=True, verbose_name='Required')),
                ('visible', models.BooleanField(default=True, verbose_name='Visible')),
                ('choices', models.CharField(help_text='Comma separated options where applicable. If an option itself contains commas, surround the option with `backticks`.', max_length=1000, verbose_name='Choices', blank=True)),
                ('default', models.CharField(max_length=2000, verbose_name='Default value', blank=True)),
                ('placeholder_text', models.CharField(max_length=100, verbose_name='Placeholder Text', blank=True)),
                ('help_text', models.CharField(max_length=100, verbose_name='Help text', blank=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Field',
                'verbose_name_plural': 'Fields',
            },
        ),
        migrations.CreateModel(
            name='FieldEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_id', models.IntegerField()),
                ('value', models.CharField(max_length=2000, null=True)),
            ],
            options={
                'verbose_name': 'Form field entry',
                'verbose_name_plural': 'Form field entries',
            },
        ),
    ]
