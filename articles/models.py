# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
# Create your models here.
from blogs.models import Blogs
from django.conf import settings
from django.utils import timezone

class Articles(models.Model):
    title = models.CharField(max_length=150, verbose_name="Tytul")
    content = models.TextField(verbose_name="Tekst")
    published = models.DateTimeField(verbose_name="Data publikacji",auto_now=True)
    image = models.FileField(upload_to="images",verbose_name="Obrazy",default=None,null=True,blank=True)
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.DO_NOTHING)
    isProtected = models.BooleanField(default=False)
    password = models.CharField(max_length=32, null=True, )

    def __unicode__(self):
        return self.title



class Comment(models.Model):
    user = models.CharField(max_length=150, verbose_name="Uzytkownik")
    content = models.TextField(verbose_name="Tekst")
    published = models.DateTimeField(verbose_name="Data publikacji", auto_now=True,null=True)
    article = models.ForeignKey(Articles,on_delete=models.CASCADE,)

    def __unicode__(self):
        return self.user
