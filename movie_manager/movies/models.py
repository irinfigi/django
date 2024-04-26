from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(null=True)
    description=models.TextField()
    poster = models.ImageField(upload_to='images/', blank=True)  # Make sure to include 'blank=True' if the field is optional
class Director(models.Model):
    name=models.CharField(max_length=300)