# Generated by Django 2.0.3 on 2018-08-24 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_embed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text_embed',
            name='afterimg',
            field=models.ImageField(upload_to='Text_Embed_img_after/'),
        ),
        migrations.AlterField(
            model_name='text_embed',
            name='beforeimg',
            field=models.ImageField(upload_to='Text_Embed_img_before/'),
        ),
    ]