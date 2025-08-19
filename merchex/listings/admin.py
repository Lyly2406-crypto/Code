from django.contrib import admin
from .models import Band, Listing


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ("name", "genre", "year_formed", "active")  
    list_filter = ("genre", "active")  
    search_fields = ("name", "biography")  


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("genre",)  
    list_filter = ("genre",)