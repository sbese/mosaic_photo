# Generated by Django 3.0.2 on 2020-01-19 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosaic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='url',
            field=models.TextField(unique=True),
        ),
    ]
