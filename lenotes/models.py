from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length = 40, default="example group")
    intro = models.CharField(max_length = 200, default="no introduce")
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name='group_owner')
    members = models.ManyToManyField(User)
    profile = models.ImageField(upload_to='group/img', default='group/img/default.jpg')
    def __str__(self):
        return self.name

class Diary(models.Model):
    content = MarkdownxField()
    date_added = models.DateTimeField(auto_now_add = True)
    group = models.ForeignKey(Group,on_delete = models.CASCADE)
    def __str__(self):
        return self.content[:30] + '...'

class Invitation(models.Model): 
    invite_id = models.CharField(max_length = 40) 
    message = models.CharField(max_length = 200)  
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add = True)
    groupid = models.IntegerField()
    is_Read = models.BooleanField(default = False)
    def __str__(self):
        return self.message

class Imgele(models.Model):
    belong = models.ForeignKey(Diary, on_delete=models.CASCADE)
    idname = models.CharField(max_length = 40)
    img = models.ImageField(upload_to='diary/img')
    zindex = models.IntegerField(default = 999)
    w = models.IntegerField(default = 30)
    h = models.IntegerField(default = 30)
    x = models.IntegerField(default = 0)
    y = models.IntegerField(default = 0)


class Textele(models.Model):
    belong = models.ForeignKey(Diary, on_delete=models.CASCADE)
    idname = models.CharField(max_length = 40)
    content = models.TextField(default='Input something please')
    x = models.IntegerField(default = 0) 
    y = models.IntegerField(default = 0)
    fontsize = models.IntegerField(default = 40)
    fontcolor = models.CharField(max_length = 20, default='red')
    zindex = models.IntegerField(default = 999)




