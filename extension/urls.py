from django.urls import path

from extension import views

app_name = 'extension'

urlpatterns = [

    path('extend/', views.extend, name = 'extend'),
    
    path('about_us/', views.about_us, name = 'about_us'),

    path('embedding_info/', views.embedding_info, name = 'embedding_info'),

    path('extract_info/', views.extract_info, name = 'extract_info'),

]
