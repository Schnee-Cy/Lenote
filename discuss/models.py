from django.db import models
from markdownx.models import MarkdownxField
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length = 40, default="Undefined")
    content = MarkdownxField()
    date_added = models.DateTimeField(auto_now_add = True)
    topic_owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name='topic_owner')
    def __str__(self):
        return self.name

class Discuss(models.Model):
    content = MarkdownxField()
    mention = models.CharField(max_length = 60, default="")
    date_added = models.DateTimeField(auto_now_add = True)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    discuss_owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name='discuss_owner')