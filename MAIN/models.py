from django.db import models

# Create your models here.
class Data(models.Model):
    bulan = models.CharField(max_length=20)
    data = models.IntegerField()

    def __str__(self):
        return self.bulan