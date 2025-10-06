from django.contrib import admin
from .models import NewsArticle

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'author')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_date'