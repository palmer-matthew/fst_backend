from django.db import models

# Create your models here.


class TestModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return  self.first_name  + ' ' + self.last_name

class Contact(models.Model):
    name = models.CharField(max_length=255, unique=True)
    #phone = models.ForeignKey(PhoneNumber,on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=50, default="", blank=True)
    fax = models.CharField(max_length=255, default="", blank=True)
    website = models.CharField(max_length=255, default="", blank=True)
    description = models.CharField(max_length=255, default="", blank=True)
    DEPARTMENT = [
        ('CHEM','Chemistry'),
        ('COMP','Computing'),
        ('GEO', 'Geography and Geology'),
        ('LIFE', 'Life Sciences'),
        ('MATH', 'Mathematics'),
        ('PHYS', 'Physics'),
        ('OTHER', 'Other')
    ]
    department = models.CharField(max_length=5,choices=DEPARTMENT)
    CONTACT_TYPE= [
        ('EMERGENCY','Emergency'),
        ('OFFICE', 'Office'),
        ('FACULTY_STAFF', 'Faculty/Staff'),        
        ('OTHER','Other')
    ]
    contact_type = models.CharField(max_length=13, choices=CONTACT_TYPE)

    def __str__(self):
        return self.name + ('' if not self.description else ', '+self.description)

    def __unicode__(self):
        return self.name

class PhoneNumber(models.Model):
    phone = models.CharField(max_length=30, unique=True)
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE, null=True, related_name='phone_contact_set')
    PLATFORMS = [
        ('TEXT_CALL', 'Text/Call'),
        ('WHATSAPP', 'Text/WhatsApp/Call')        
    ]
    platforms = models.CharField(max_length=9, choices=PLATFORMS, null=True, default='TEXT/CALL')

    def __str__(self):
        return self.phone

    def __unicode__(self):
        return self.phone

class Scholarship(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default = "")
    details = models.TextField(default = "")

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length = 150)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    location = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class NewsFeed(models.Model):
    title = models.TextField(default = "")
    date = models.DateField()
    story = models.TextField(default = "")
    
    def __str__(self):
        return self.title