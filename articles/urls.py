from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static


from . import views

app_name= 'article'
urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    path('showall/', views.articles, name='articles'),
    path('<int:article_id>/', views.article, name='article'),

    path('<int:a_id>/addcomment', views.addcomment, name='addcomment'),

]