from django.contrib import admin
from .models import NewsPost

# Register your models here.

@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'description', 'author')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
