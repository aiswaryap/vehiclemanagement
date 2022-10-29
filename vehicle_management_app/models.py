from django.db import models

# Create your models here.
class vehicle(models.Model):
    number=models.CharField(max_length=100)
    type=models.IntegerField()
    model=models.TextField()
    description=models.TextField()