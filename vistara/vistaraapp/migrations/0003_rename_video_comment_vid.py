# Generated by Django 3.2.6 on 2021-11-18 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vistaraapp', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='video',
            new_name='vid',
        ),
    ]