from django.contrib import admin
from core.models import TestModel
from core.models import Contact

# Register your models here.

admin.site.register(TestModel)
admin.site.register(Contact)