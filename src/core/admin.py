from django.contrib import admin
from src.core.models import TestModel
from src.core.models import Contact
from src.core.models import Scholarship
from src.core.models import PhoneNumber
from src.core.models import Event

# Register your models here.

admin.site.register(TestModel)
#admin.site.register(Contact)
admin.site.register(Scholarship)
#admin.site.register(PhoneNumber)

class PhoneNumberInline (admin.TabularInline):
    model = PhoneNumber
    extra = 0

class ContactInline(admin.ModelAdmin):
    inlines = [
        PhoneNumberInline,
    ]


admin.site.register(Contact,ContactInline)
admin.site.register(Event)
