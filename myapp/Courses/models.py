from django.db import models

# Create your models here.

class CourseData(models.Model):
    poster = models.ImageField(upload_to="images/")
    name =  models.CharField(max_length=50)
    instructor = models.CharField(max_length=30)
    duration= models.CharField(max_length=30)
    price = models.FloatField()