# Generated by Django 2.2.1 on 2019-05-28 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_converter', '0003_auto_20190528_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='url',
            field=models.URLField(verbose_name='link'),
        ),
    ]
