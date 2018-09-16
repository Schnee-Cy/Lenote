from django.urls import path

from discuss import views

app_name = 'discuss'

urlpatterns = [

    # 讨论区主页，每个主页显示10条Topic
    path('topics/', views.topics, name = 'topics'),

    # 创建新的Topic
    path('new_topic/', views.new_topic, name = 'new_topic'),

    # 显示Topic详细内容，按每页20条显示评论，可编辑添加评论
    path('topic/<int:topic_id>', views.topic, name = 'topic'),

    path('edit_topic/<int:topic_id>', views.edit_topic, name = 'edit_topic'),

    path('del_topic/<int:topic_id>', views.del_topic, name = 'del_topic'),

    path('new_discuss/<int:topic_id>', views.new_discuss, name = 'new_discuss'),

    path('del_discuss/<int:topic_id>/<int:dis_id>', views.del_discuss, name = 'del_discuss'),
]
