# Generated by Django 3.2.7 on 2021-10-23 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RumahSakit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=40)),
                ('alamat', models.CharField(max_length=60)),
                ('kapasitas', models.IntegerField()),
                ('isi', models.IntegerField()),
            ],
        ),
    ]
