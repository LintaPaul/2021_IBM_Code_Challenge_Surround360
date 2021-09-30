from django.db import models

from django.utils import timezone
# Create your models here.
class Official(models.Model):
    DEPTS=(('W',"Water"),('E',"Electricity"),('R',"Roads"))
    SUBDEPS = (('WL', "Water Leaks"), ("SL", "Shortage of supply"),('PF', "Power failure"), ('LB', "Line damage"), ('RD', "Road damage"),('TR', "Tarring required"))
    region=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=1,choices=DEPTS)
    subdept=models.CharField(max_length=2,choices=SUBDEPS)
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
    
    landmark=models.CharField(max_length=100, default="na")
    #lat=models.DecimalField(decimal_places=6,max_digits=18,default="10.2345")
    sender=models.CharField(max_length=30,default="Nill")
    status=models.CharField(max_length=2,choices=STATUS,default="US")
    
class Tourist(models.Model):
    location = models.CharField(max_length = 180)
    review = models.CharField(max_length = 500)
    rating = models.IntegerField()  
    #postdate = models.DateTimeField(default = timezone.now)            #out of 5
    image = models.ImageField(upload_to = 'trial/images/')   #path to image



