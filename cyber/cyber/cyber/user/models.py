from django.db import models

# Create your models here.
class usermodel(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    images = models.FileField(upload_to='files/')
    
    class Meta:
        db_table = "usermodel"