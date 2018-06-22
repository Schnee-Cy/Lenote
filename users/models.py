from django.db import models
from django.contrib.auth.models import User
from lenotes.models import Group
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class UserInfo(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 20, default = "Undefined")
    gender = models.CharField(max_length = 6, choices = GENDER_CHOICES, default = "Male")
    email = models.CharField(max_length = 40, default = "Undefined@example.com")
    intro = models.CharField(max_length = 200, default = "hello world")
    profile = ProcessedImageField(upload_to='user/img', default='user/img/default.jpg', 
        processors=[ResizeToFill(500, 500)],  format='JPEG', options={'quality': 60})
    unread_count = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.CharField(max_length = 20)
    text = models.CharField(max_length = 300)
    date_added = models.DateTimeField(auto_now_add = True)
    receiver = models.ForeignKey(User, on_delete = models.CASCADE)
    is_Read = models.BooleanField(default = False)
    def __str__(self):
        return self.text

