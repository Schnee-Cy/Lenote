# Generated by Django 2.0.3 on 2018-08-24 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lenotes', '0017_merge_20180824_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='diary_log',
            field=models.TextField(default='2018-08-24 23:03:56.284241  Create diary'),
        ),
    ]