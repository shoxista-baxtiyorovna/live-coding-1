from django.contrib import admin
from .models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'name']
    search_field = [ 'name' ]
    prepopulated_fields = {"slug": ("name",)}

