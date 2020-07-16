from django.db import models

# Create your models here.


class TestModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return  self.first_name  + ' ' + self.last_name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    fax = models.CharField(max_length=255,default="")
    website = models.CharField(max_length=255)

    def __str__(self):
        return self.name
