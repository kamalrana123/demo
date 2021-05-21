# Generated by Django 3.2.3 on 2021-05-21 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('BTech', 'BTech'), ('MTech', 'MTech'), ('MCA', 'MCA'), ('MSc', 'MSc'), ('MBA', 'MBA'), ('Ph.D', 'Ph.D')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(choices=[('BTech', 'BTech'), ('MTech', 'MTech'), ('MCA', 'MCA'), ('MSc', 'MSc'), ('MBA', 'MBA'), ('Ph.D', 'Ph.D')], max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='documents/')),
            ],
        ),
    ]
