from django.contrib import admin
from .models import ProductItem, Profile, Event, Occurence

# Register your models here.

class OccurenceInline (admin.TabularInline):
	model = Occurence
	extra = 1

class EventAdmin(admin.ModelAdmin):
	inlines=[OccurenceInline]
	

admin.site.register(ProductItem)
admin.site.register(Profile)
admin.site.register(Event, EventAdmin)

