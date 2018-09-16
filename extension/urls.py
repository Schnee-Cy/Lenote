from django.urls import path

from extension import views

app_name = 'extension'

urlpatterns = [

    path('extend/', views.extend, name = 'extend'),
    
    path('about_us/', views.about_us, name = 'about_us'),

    path('embedding_info/', views.embedding_info, name = 'embedding_info'),

    path('extract_info/', views.extract_info, name = 'extract_info'),

    path('image_cutting/', views.image_cutting, name = 'image_cutting'),

    path('character_image/', views.character_image, name = 'character_image'),

    path('online_hash_verify/', views.online_hash_verify, name = 'online_hash_verify'),

    path('download_hash_verify/', views.download_hash_verify, name = 'download_hash_verify'),

    path('bagels/', views.bagels, name = 'bagels'),

    path('tiny_fish/', views.tiny_fish, name = 'tiny_fish'),
]
