from django.contrib import admin
from core.models import TestModel
from core.models import Contact
from core.models import Scholarship
from core.models import PhoneNumber
from core.models import Event
from core.models import NewsFeed

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
admin.site.register(NewsFeed)

