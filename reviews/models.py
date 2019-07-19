from django.db import models
import numpy as np
# Create your models here.
 
class Category(models.Model):
    category_name=models.CharField(max_length=50)

class Hotel(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=150)


class Review(models.Model):
    RATING_CHOICES=(
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    )
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    pub_date=models.DateTimeField('date published')
    user_name=models.CharField(max_length=200)
    comment=models.CharField(max_length=250)
    rating=models.IntegerField(choices=RATING_CHOICES)

