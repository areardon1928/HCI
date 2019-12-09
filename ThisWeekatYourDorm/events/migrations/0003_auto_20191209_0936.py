# Generated by Django 3.0 on 2019-12-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20191209_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='author',
            field=models.CharField(default='areardon', max_length=50, verbose_name='Author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='Keenan Basement', max_length=50, verbose_name='Event Location'),
            preserve_default=False,
        ),
    ]
