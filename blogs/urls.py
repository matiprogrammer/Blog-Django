from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static


from . import views
app_name= 'blogs'
urlpatterns = [
    path('showall/', views.blogs, name='blogs'),
    path('<int:blog_id>/', views.blog, name='blog'),
    path('new/',views.post_new,name='post_new'),
]