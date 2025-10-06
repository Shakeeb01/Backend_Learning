from django.contrib import admin
from .models import Author,Post

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','age','email']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','content','created_at','updated_at','author']
    search_fields = ['title', 'content']
    list_filter = ['author', 'created_at']