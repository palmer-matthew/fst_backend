from django.contrib import admin
from core.models import TestModel
from core.models import Contact
from core.models import Scholarship
from core.models import PhoneNumber
from core.models import Event
from core.models import NewsFeed
from core.models import Position
from core.models import GeometryObject
from core.models import GeoJSONFeature

from django.urls import reverse
from django.utils.safestring import mark_safe
import nested_admin

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

class PositionInline (nested_admin.NestedStackedInline):
    model = Position
    extra = 0

class GeometryObjectInline(nested_admin.NestedTabularInline):
    model = GeometryObject
    extra = 1
    inlines = [PositionInline]

class GeoJSONFeatureModelAdmin(nested_admin.NestedModelAdmin):
    inlines = [GeometryObjectInline]

admin.site.register(GeoJSONFeature, GeoJSONFeatureModelAdmin)
admin.site.register(Contact,ContactInline)
admin.site.register(Event)
admin.site.register(NewsFeed)

