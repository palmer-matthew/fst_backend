from django.db import models

# Create your models here.


class TestModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return  self.first_name  + ' ' + self.last_name


class PhoneNum(models.Model):
    number = models.CharField(max_length=30)

    def __str__(self):
        return self.number

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    phone = models.ForeignKey(PhoneNum, on_delete=models.CASCADE)
    fax = models.CharField(max_length=255,default="",blank=True)
    website = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Scholarship(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default = "")
    details = models.TextField(default = "")

    def __str__(self):
        return self.name
