from django.db import models

# Create your models here.
class Hareket(models.Model):  
    name = models.CharField(max_length=180, verbose_name="Hareket İsmi", default="newaction")
    slug = models.SlugField(max_length=200, unique=True, null=True)
    activity = models.IntegerField(verbose_name="Aktiflik", default=0)

    def __str__(self):
        return self.name