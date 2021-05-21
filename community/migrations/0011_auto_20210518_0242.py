# Generated by Django 3.2.3 on 2021-05-18 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
        ('community', '0010_communityquestion_stu_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityanswer',
            name='downvote',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='communityanswer',
            name='upvote',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='communityanswer',
            name='student_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.signup'),
        ),
    ]