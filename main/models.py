from django.db import models


class Price(models.Model):
    name = models.CharField(max_length=100)
    price = models.TextField()
    

