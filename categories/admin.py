from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'name']
    search_field = [ 'name', 'description']
    prepopulated_fields = {"slug": ("name",)}
