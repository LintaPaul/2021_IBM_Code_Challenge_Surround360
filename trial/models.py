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
    phoneno=models.IntegerField(primary_key=True)
    region=models.CharField(max_length=50)

class Complaints(models.Model):
    DEPTS=(('W',"Water"),('E',"Electricity"),('R',"Roads"))
    STATUS=(("US","unsolved"),("S","solved"))
    region=models.CharField(max_length=50)
    dept=models.CharField(max_length=1,choices=DEPTS)
    category=models.CharField(max_length=30)
    complaint=models.CharField(max_length=1000)
    status=models.CharField(max_length=2,choices=STATUS)
    
class tourist(models.Model):
    location = models.CharField(max_length = 180)
    review = models.CharField(max_length = 500)
    rating = models.IntegerField()              #out of 5
    image = models.ImageField(upload_to = '')   #path to image



