from django.db import models

# Create your models here.

class Home(models.Model):
    foto = models.CharField(max_length=255, default="")
    nama = models.CharField(max_length=255, default="")
    harga = models.IntegerField(default=0)

    def __str__(self):
        return self.nama  


class Description(models.Model):
    home = models.ForeignKey(Home,on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.home.nama 