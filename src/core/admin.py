from django.contrib import admin
from core.models import TestModel
from core.models import Contact
from core.models import Scholarship
from core.models import Event

# Register your models here.

admin.site.register(TestModel)
admin.site.register(Contact)
admin.site.register(Scholarship)
admin.site.register(Event)
