# Generated by Django 3.0.2 on 2020-01-19 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('r', models.IntegerField()),
                ('g', models.IntegerField()),
                ('b', models.IntegerField()),
            ],
        ),
    ]