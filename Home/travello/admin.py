from django.contrib import admin
from .models import Destination, Testimonial, Slide

# Register your models here.

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'offer')
    list_filter = ('offer',)
    search_fields = ('name', 'description')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment')
    search_fields = ('name', 'comment')

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')
    search_fields = ('title',)