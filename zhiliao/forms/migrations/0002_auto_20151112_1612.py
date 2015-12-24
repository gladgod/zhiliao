# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import zhiliao.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', zhiliao.core.fields.RichTextField(verbose_name='Content')),
                ('button_text', models.CharField(max_length=50, verbose_name='Button text', blank=True)),
                ('response', zhiliao.core.fields.RichTextField(verbose_name='Response')),
                ('send_email', models.BooleanField(default=True, help_text='To send an email to the email address supplied in the form upon submission, check this box.', verbose_name='Send email to user')),
                ('email_from', models.EmailField(help_text='The address the email will be sent from', max_length=254, verbose_name='From address', blank=True)),
                ('email_copies', models.CharField(help_text='Provide a comma separated list of email addresses to be notified upon form submission. Leave blank to disable notifications.', max_length=200, verbose_name='Send email to others', blank=True)),
                ('email_subject', models.CharField(max_length=200, verbose_name='Subject', blank=True)),
                ('email_message', models.TextField(help_text='Emails sent based on the above options will contain each of the form fields entered. You can also enter a message here that will be included in the email.', verbose_name='Message', blank=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Form',
                'verbose_name_plural': 'Forms',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='FormEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_time', models.DateTimeField(verbose_name='Date/time')),
                ('form', models.ForeignKey(related_name='entries', to='forms.Form')),
            ],
            options={
                'verbose_name': 'Form entry',
                'verbose_name_plural': 'Form entries',
            },
        ),
        migrations.AddField(
            model_name='fieldentry',
            name='entry',
            field=models.ForeignKey(related_name='fields', to='forms.FormEntry'),
        ),
        migrations.AddField(
            model_name='field',
            name='form',
            field=models.ForeignKey(related_name='fields', to='forms.Form'),
        ),
    ]
