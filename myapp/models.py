from django.db import models

class user(models.Model):
    name = models.CharField(max_length=50 )
    Contact = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class ajax(models.Model):
    name = models.CharField(max_length=200)
    password= models.CharField(max_length=200,default = None)
    dob = models.DateField()

    def __str__(self):
        return self.name
