from django.db import models

# Create your models here.
class Correction(models.Model):
    code=models.CharField(max_length=7) 
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
