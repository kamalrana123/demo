# Generated by Django 3.2.3 on 2021-05-21 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0013_alter_communityanswer_answer_assets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communityanswer',
            name='answer_assets',
        ),
    ]
