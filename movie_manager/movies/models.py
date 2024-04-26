from django.db import models

# Create your models here.
class CensorInfo(models.Model):
    rating=models.CharField(max_length=10)
    cirtified_by=models.CharField(max_length=200,null=True)
class MovieInfo(models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(null=True)
    description=models.TextField()
    poster = models.ImageField(upload_to='images/', blank=True)  # Make sure to include 'blank=True' if the field is optional
    censor_details=models.OneToOneField(CensorInfo,on_delete=models.SET_NULL,related_name='movie',null=True)
    def __str__(self):
        return self.title
class Director(models.Model):
    name=models.CharField(max_length=300)