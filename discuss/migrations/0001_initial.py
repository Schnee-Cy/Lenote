# Generated by Django 2.0.3 on 2018-09-13 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discuss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', markdownx.models.MarkdownxField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('discuss_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discuss_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Undefined', max_length=40)),
                ('content', markdownx.models.MarkdownxField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('topic_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='discuss',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discuss.Topic'),
        ),
    ]
