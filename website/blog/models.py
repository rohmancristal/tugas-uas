from django.db import models

# Create your models here.
class blog(models.Model):
    judul = models.CharField(max_length=255)
    body  = models.TextField()
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.judul