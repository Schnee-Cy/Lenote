# Generated by Django 2.0.3 on 2018-06-21 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lenotes', '0010_diary_diary_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='diary_log',
            field=models.TextField(default='2018-06-21 16:23:38.256891  Create diary'),
        ),
    ]
