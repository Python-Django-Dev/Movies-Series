from django.db import models
from datetime import datetime

# Create your models here.





class Film(models.Model):
    name = models.CharField(max_length = 100)
    rating = models.DecimalField(max_digits = 2,decimal_places = 1,null = True,blank = True)
    image = models.ImageField(upload_to = 'photos/%y/%m/%d',null = True)
    movie_link = models.TextField(null = True)
    movie_trailer = models.CharField(max_length = 1000,null = True)
    date_and_time = models.DateTimeField(default = datetime.now)
    active = models.BooleanField(default = True)
    class Meta:
        verbose_name = 'Movie'
    def __str__(self):
        return self.name
    
class Login(models.Model):
    name = models.CharField(max_length = 40,null= True)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 40)
    date_and_time = models.DateTimeField(default = datetime.now)

    class Meta:
        verbose_name = 'User'
    def __str__(self):
        return self.email

