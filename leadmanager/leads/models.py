from django.db import models

# Create your models here.


class Lead(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField
    descr = models.TextField(max_length=500)
    amount = models.IntegerField
    producer = models.TextField(max_length=100)
    rating = models.IntegerField
    # id = models.
    # comments = 
    # wantToBuy =
    # specificParameters =   
    status = models.TextField(max_length=15)
