from django.db import models

# Create your models here.
class shop(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    desc=models.TextField()
    img=models.ImageField(upload_to="imagess")
    price=models.IntegerField()
