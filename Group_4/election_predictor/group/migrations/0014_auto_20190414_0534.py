# Generated by Django 2.1.7 on 2019-04-14 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_merge_20190407_1234'),
        ('group', '0013_auto_20190413_2133'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event_Forum',
            new_name='EventForum',
        ),
    ]
