# Generated by Django 4.1.5 on 2023-01-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=200)),
                ('kitob_haqida', models.TextField()),
                ('muallif', models.CharField(max_length=200)),
                ('janr', models.CharField(max_length=100)),
                ('isbn', models.IntegerField()),
                ('narx', models.IntegerField()),
            ],
        ),
    ]
