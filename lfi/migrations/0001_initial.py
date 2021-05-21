# Generated by Django 3.2.3 on 2021-05-20 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0002_alter_signup_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoundItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now=True)),
                ('item_description', models.CharField(max_length=2000)),
                ('item_type', models.CharField(choices=[('metal', 'metal'), ('plastic', 'plastic'), ('wooden', 'wooden'), ('leather', 'leather'), ('cloth', 'cloth'), ('mix', 'mix'), ('chemicals', 'chemicals')], default='mix', max_length=2000)),
                ('lost_place', models.CharField(blank=True, max_length=100, null=True)),
                ('lost_time', models.TimeField()),
                ('lost_date', models.DateField(auto_now=True)),
                ('item_price', models.IntegerField()),
                ('item_color', models.CharField(choices=[('mix', 'mix'), ('transparent', 'transparent'), ('translucent', 'translucent'), ('grey', 'grey'), ('purple', 'purple'), ('gold', 'gold'), ('silver', 'silver'), ('white', 'white'), ('pink', 'pink'), ('orange', 'orange'), ('brown', 'brown'), ('black', 'black'), ('green', 'green'), ('yellow', 'yellow'), ('blue', 'blue'), ('red', 'red')], default='mix', max_length=20)),
                ('shape', models.CharField(choices=[('other', 'other'), ('circle', 'circle'), ('kite', 'kite'), ('shape-changer', 'shape-changer'), ('cube', 'cube'), ('cuboid', 'cuboid'), ('sphere', 'sphere'), ('cylindrical', 'cylindrical'), ('cone', 'cone'), ('pyramid', 'pyramid'), ('square', 'square'), ('rectangle', 'rectangle'), ('triangle', 'triangle')], default='other', max_length=20)),
                ('author_name', models.CharField(blank=True, max_length=20, null=True)),
                ('company_type', models.CharField(blank=True, choices=[('branded', 'branded'), ('local', 'local')], default='local', max_length=20, null=True)),
                ('item_pic1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='pic1')),
                ('status', models.CharField(choices=[('available', 'available'), ('delivered', 'delivered')], default='available', max_length=20)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register.signup')),
            ],
        ),
        migrations.CreateModel(
            name='LostItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now=True)),
                ('item_description', models.CharField(max_length=2000)),
                ('item_type', models.CharField(choices=[('metal', 'metal'), ('plastic', 'plastic'), ('wooden', 'wooden'), ('leather', 'leather'), ('cloth', 'cloth'), ('mix', 'mix'), ('chemicals', 'chemicals')], default='mix', max_length=2000)),
                ('lost_place', models.CharField(blank=True, max_length=100, null=True)),
                ('lost_time', models.TimeField()),
                ('lost_date', models.DateField(auto_now=True)),
                ('item_price', models.IntegerField()),
                ('item_color', models.CharField(choices=[('mix', 'mix'), ('transparent', 'transparent'), ('translucent', 'translucent'), ('grey', 'grey'), ('purple', 'purple'), ('gold', 'gold'), ('silver', 'silver'), ('white', 'white'), ('pink', 'pink'), ('orange', 'orange'), ('brown', 'brown'), ('black', 'black'), ('green', 'green'), ('yellow', 'yellow'), ('blue', 'blue'), ('red', 'red')], default='mix', max_length=20)),
                ('shape', models.CharField(choices=[('other', 'other'), ('circle', 'circle'), ('kite', 'kite'), ('shape-changer', 'shape-changer'), ('cube', 'cube'), ('cuboid', 'cuboid'), ('sphere', 'sphere'), ('cylindrical', 'cylindrical'), ('cone', 'cone'), ('pyramid', 'pyramid'), ('square', 'square'), ('rectangle', 'rectangle'), ('triangle', 'triangle')], default='other', max_length=20)),
                ('author_name', models.CharField(blank=True, max_length=20, null=True)),
                ('company_type', models.CharField(blank=True, choices=[('branded', 'branded'), ('local', 'local')], default='local', max_length=20, null=True)),
                ('item_pic1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='pic1')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register.signup')),
            ],
        ),
        migrations.CreateModel(
            name='Matching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_percent', models.IntegerField(default=0)),
                ('found_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lfi.founditem')),
                ('lost_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lfi.lostitem')),
            ],
        ),
    ]