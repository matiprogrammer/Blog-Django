from django.db import models
from django.conf import settings
# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=150, verbose_name="Tytul")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, verbose_name="Uzytkownik", on_delete=models.DO_NOTHING)


    def __unicode__(self):
        return self.title
