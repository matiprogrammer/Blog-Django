"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import user_login,success,user_logout,user_create,user_create_success,logout,test

app_name='blog'
urlpatterns = [
    path('blog/', include('blogs.urls')),
    path('article/', include('articles.urls')),
    path('tes/', views.tes, name='tes'),
    path('admin/', admin.site.urls),
    path('login/',user_login,name='user_login'),
    path('', success, name='success'),
    path('logout/', user_logout, name='user_logout'),
    path('register/',user_create,name='user_create'),
    path('register/success',user_create_success,name='user_create_success'),
    path('test',test,name='test'),

              ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


