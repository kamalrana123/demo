# Generated by Django 3.2.3 on 2021-05-21 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0011_auto_20210518_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityanswer',
            name='answer_assets',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]
