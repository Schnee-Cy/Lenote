# Generated by Django 2.0.3 on 2018-08-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lenotes', '0014_auto_20180630_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='diary_log',
            field=models.TextField(default='2018-08-24 16:56:44.555673  Create diary'),
        ),
    ]
