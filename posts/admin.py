from django.contrib import admin
from .models import Post as POST
# Register your models here.
@admin.register(POST)
class POSTAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'author', 'publish', 'created', 'updated')
    list_filter = ('author', 'publish', 'created', 'updated')
    
