from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'title', 'author', 'category', 'status']
    search_field = [ 'title', 'content' ]
    prepopulated_fields = {"slug": ("title",)}


