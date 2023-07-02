from django.db import models

# Create your models here.
#crear una clase para guardar una imagen en la base de datos
class Jobs(models.Model):
    image = models.ImageField(upload_to='images/')
    sumary = models.CharField(max_length=200)

    def __str__(self):
        return self.sumary