# Generated by Django 3.2.12 on 2022-04-08 19:19

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_userprofile_recap_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackoffEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The moment when the item was created.')),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True, help_text='The last moment when the item was modified. A value in year 1750 indicates the value is unknown')),
                ('email_address', models.EmailField(help_text="The backoff event is related to this email address instead of a user, in this way, if users change their email address this won't affect the user's new email address, this unique.", max_length=254, unique=True)),
                ('retry_counter', models.SmallIntegerField(help_text='The retry counter for exponential backoff events.')),
                ('next_retry_date', models.DateTimeField(help_text='The next retry datetime for exponential backoff events.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmailFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The moment when the item was created.')),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True, help_text='The last moment when the item was modified. A value in year 1750 indicates the value is unknown')),
                ('email_address', models.EmailField(help_text="EmailFlag object is related to this email address instead of a user, in this way, if users change their email address this won't affect the user's new email address.", max_length=254)),
                ('object_type', models.SmallIntegerField(choices=[(0, 'Email ban'), (1, 'Email flag')], help_text='The object type assigned, Email ban: ban an email address and avoid sending any email. Email flag: flag an email address for a special treatment.')),
                ('flag', models.SmallIntegerField(blank=True, choices=[(0, 'small_email_only'), (1, 'max_retry_reached')], help_text='The actual flag assigned, e.g: small_email_only.', null=True)),
                ('event_sub_type', models.SmallIntegerField(choices=[(0, 'Undetermined'), (1, 'General'), (2, 'NoEmail'), (3, 'Suppressed'), (4, 'OnAccountSuppressionList'), (5, 'MailboxFull'), (6, 'MessageTooLarge'), (7, 'ContentRejected'), (8, 'AttachmentRejected'), (9, 'Complaint'), (10, 'Other')], help_text='The SNS bounce subtype that triggered the object.')),
            ],
        ),
        migrations.CreateModel(
            name='EmailSent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The moment when the item was created.')),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True, help_text='The last moment when the item was modified. A value in year 1750 indicates the value is unknown')),
                ('message_id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique message identifier')),
                ('from_email', models.CharField(help_text='From email address', max_length=300)),
                ('to', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=254), blank=True, help_text='List of email recipients', null=True, size=None)),
                ('bcc', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=254), blank=True, help_text='List of BCC emails addresses', null=True, size=None)),
                ('cc', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=254), blank=True, help_text='List of CC emails addresses', null=True, size=None)),
                ('reply_to', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=254), blank=True, help_text='List of Reply to emails addresses', null=True, size=None)),
                ('subject', models.TextField(blank=True, help_text='Subject')),
                ('plain_text', models.TextField(blank=True, help_text='Plain Text Message Body')),
                ('html_message', models.TextField(blank=True, help_text='HTML Message Body')),
                ('headers', models.JSONField(blank=True, help_text='Original email Headers', null=True)),
                ('user', models.ForeignKey(blank=True, help_text="The user that this message is related to in case of users change their email address we can send failed email to the user's new email address, this is optional in case we send email to anemail address that doesn't belong to a CL user.", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emails', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='emailflag',
            index=models.Index(fields=['email_address'], name='users_email_email_a_624792_idx'),
        ),
        migrations.AddConstraint(
            model_name='emailflag',
            constraint=models.UniqueConstraint(condition=models.Q(('object_type', 0)), fields=('email_address',), name='unique_email_ban'),
        ),
        migrations.AddIndex(
            model_name='emailsent',
            index=models.Index(fields=['message_id'], name='users_email_message_f49e38_idx'),
        ),
    ]
