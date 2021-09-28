from django.db import models

# Create your models here.
class Official(models.Model):
    region=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    subdept=models.CharField(max_length=50)
    empid=models.CharField(max_length=10, primary_key=True)
    phoneno=models.IntegerField()
    score=models.IntegerField()


class Public(models.Model):
    name=models.CharField(max_length=30)
    phoneno=models.IntegerField()
    region=models.CharField(max_length=50)

class tourist(models.Model):
    location = models.CharField(max_length = 180)
    review = models.CharField(max_length = 500)
    rating = models.IntegerField()              #out of 5
    image = models.ImageField(upload_to = '')   #path to image



