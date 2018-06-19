from django.contrib import admin
# Register your models here.
from lenotes.models import *
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Group)
# admin.site.register(Diary)
admin.site.register(Invitation)
admin.site.register(Imgele)
admin.site.register(Textele)
admin.site.register(Diary, MarkdownxModelAdmin)
