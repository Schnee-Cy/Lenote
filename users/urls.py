from django.urls import path

from users import views
app_name = 'users'

urlpatterns = [
    #login
    path('login/', views.login_view, name = 'login'),
    #logout
    path('logout/', views.logout_view, name = 'logout'),
    #register
    path('register/', views.register, name = 'register'),
    
    path('home/', views.home, name = 'home'),

    path('notice/', views.notice, name = 'notice'),

    path('settings/', views.settings, name = 'settings'),

    path('reset_password/', views.reset_password, name = 'reset_password'),

	path('reset_done/', views.reset_done, name = 'reset_done'),

    path('send_message/', views.send_message, name = 'send_message'),

    path('read_message/<int:message_id>', views.read_message, name = 'read_message'),

    path('del_message/<int:message_id>', views.del_message, name = 'del_message'),

    path('deal_invi/<int:invi_id><int:accept>',views.deal_invi, name = 'deal_invi' ),

    path('quit_group/<int:group_id>', views.quit_group, name = 'quit_group'),

    path('del_invi/<int:invi_id>', views.del_invi, name = 'del_invi'),
] 
