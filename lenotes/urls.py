from django.urls import path
import django.views
from lenotes import views

app_name = 'lenotes'

urlpatterns = [
    path('', views.index, name = 'index'),
    
    #path('group/', views.groups, name = 'groups'),

    path('group/<int:group_id>', views.group, name = 'group'),

    #path('group_diary/<int:group_id>/<int:diary_id>', views.group_diary, name = 'group_diary'),

    path('diary_month/<int:group_id>/<int:year>/<int:month>/<int:styleSelect>', views.diary_month, name = 'diary_month'),

    path('manage/<int:group_id>', views.manage, name = 'manage'),
    
    path('del_member/<int:group_id><int:info_id>', views.del_member, name = 'del_member'),

    path('send_invite/<int:group_id>', views.send_invite, name = 'send_invite'),

    path('new_group/', views.new_group, name = 'new_group'),

    path('del_group/<int:group_id>', views.del_group, name = 'del_group'),

    path('new_diary/<int:group_id>', views.new_diary, name = 'new_diary'),
    
    path('del_diary/<int:diary_id>', views.del_diary, name = 'del_diary'),

    path('add_diary/<int:group_id>', views.add_diary, name = 'add_diary'),

    path('edit_diary/<int:group_id>/<int:diary_id>', views.edit_diary, name = 'edit_diary'),

    path('edit_diary_md/<int:diary_id>', views.edit_diary_md, name = 'edit_diary_md'),

    path('diary_log/<int:diary_id>', views.diary_log, name = 'diary_log'),

    path('file_download', views.file_download, name = 'file_download'),

    path('upload_ajax/', views.upload_ajax, name='upload_ajax'),

    path('delete_ajax/', views.delete_ajax, name='delete_ajax'),

]
