from django.db import models

# Create your models here.


class TestModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Contact(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # phone = models.ForeignKey(PhoneNumber,on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=50, default="", blank=True)
    fax = models.CharField(max_length=255, default="", blank=True)
    website = models.URLField(max_length=255, default="", blank=True)
    description = models.TextField(default="", blank=True)
    DEPARTMENT = [
        ("CHEM", "Chemistry"),
        ("COMP", "Computing"),
        ("GEO", "Geography and Geology"),
        ("LIFE", "Life Sciences"),
        ("MATH", "Mathematics"),
        ("PHYS", "Physics"),
        ("OTHER", "Other"),
    ]
    department = models.CharField(max_length=5, choices=DEPARTMENT)
    CONTACT_TYPE = [
        ("EMERGENCY", "Emergency"),
        ("OFFICE", "Office"),
        ("FACULTY_STAFF", "Faculty/Staff"),
        ("OTHER", "Other"),
    ]
    contact_type = models.CharField(max_length=13, choices=CONTACT_TYPE)

    def __str__(self):
        return self.name + ("" if not self.description else ", " + self.description)

    def __unicode__(self):
        return self.name


class PhoneNumber(models.Model):
    phone = models.CharField(max_length=30, unique=True)
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, null=True, related_name="phone_contact_set"
    )
    PLATFORMS = [("TEXT_CALL", "Text/Call"), ("WHATSAPP", "Text/WhatsApp/Call")]
    platforms = models.CharField(
        max_length=9, choices=PLATFORMS, null=True, default="TEXT/CALL"
    )

    def __str__(self):
        return self.phone

    def __unicode__(self):
        return self.phone


class Scholarship(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default="")
    details = models.TextField(default="")

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length = 150)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    location = models.CharField(max_length = 150)
    poster_image = models.ImageField(upload_to = 'assets/', height_field = None,\
        width_field = None, max_length = 100, default = '')

    def __str__(self):
        return self.name


class NewsFeed(models.Model):
    title = models.TextField(default="")
    date = models.DateField()
    story = models.TextField(default="")

    def __str__(self):
        return self.title


class GeoJSONFeature(models.Model):
    title = models.CharField(default='',max_length=50,unique=True)
    code = models.CharField(default='',max_length=50,unique=True)
    alt_name = models.CharField(default='',max_length=50, blank=True)
    associated_with = models.CharField(default='', max_length=50, blank=True)
    GEO_JSON_TYPES = [("Feature", "Feature")]
    geo_json_type = models.CharField(
        default="Feature", max_length=7, choices=GEO_JSON_TYPES
    )

    def __str__(self):
        return self.geo_json_type.__str__() + ' '+self.title+'/'+ self.alt_name+' '+ self.geometry.__str__()


class GeometryObject(models.Model):
    GEOMETRY_TYPES = [
        ("Point", "Point"),
        ("MultiPoint", "MultiPoint"),
        ("LineString", "LineString"),
        ("MultiLineString", "MultiLineString"),
        ("Polygon", "Polygon"),
        ("MultiPolygon", "MultiPolygon"),
        ("GeometryCollection", "GeometryCollection"),
    ]
    geometry_type = models.CharField(max_length=18, choices=GEOMETRY_TYPES)
    feature = models.OneToOneField(
        GeoJSONFeature, on_delete=models.CASCADE, related_name="geometry"
    )

    def __str__(self):
        string = "with geometry of type: "+ self.geometry_type.__str__() 
        return string


class Position(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    geometry_object = models.ForeignKey(
        GeometryObject, on_delete=models.CASCADE, related_name="coordinates"
    )
    MARKER_TYPES = [
        ('START','start'),
        ('END', 'end'),
        ('NONE', 'none')
    ]
    marker = models.CharField(max_length=5, default='NONE', choices=MARKER_TYPES)

    def __str__(self):
        return (
            self.geometry_object.__str__()
            + " with points: ["
            + self.longitude.__str__()
            + ","
            + self.latitude.__str__()
            + "]"
        )

