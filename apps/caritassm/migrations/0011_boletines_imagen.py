# Generated by Django 3.1.2 on 2020-10-24 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caritassm', '0010_auto_20201023_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='boletines',
            name='imagen',
            field=models.ImageField(null=True, upload_to='boletines'),
        ),
    ]
