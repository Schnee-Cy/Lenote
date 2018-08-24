from django.urls import path

from text_embed import views

app_name = 'text_embed'


urlpatterns = [
    path('embedding_info/', views.embedding_info, name = 'embedding_info'),

    path('extract_info/', views.extract_info, name = 'extract_info'),
]
