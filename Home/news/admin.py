from django.contrib import admin
from .models import News

# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('heading', 'category', 'date')  
    list_filter = ('category', 'date')               
    search_fields = ('heading', 'description')       
    ordering = ('-date',)                             