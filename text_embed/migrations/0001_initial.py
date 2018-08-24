# Generated by Django 2.0.3 on 2018-08-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text_Embed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=5000)),
                ('beforeimg', models.ImageField(upload_to='Text_Embed_img_before')),
                ('afterimg', models.ImageField(upload_to='Text_Embed_img_after')),
            ],
        ),
    ]
