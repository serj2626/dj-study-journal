# Generated by Django 5.0.3 on 2024-04-05 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management_app', '0003_alter_feedbackstaffs_feedback_reply_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FeedBackStaffs',
            new_name='FeedBackStaff',
        ),
    ]
