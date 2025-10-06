from django.contrib import admin
from .models import Division, Leadership, Award, Event, AboutPage, ContactInquiry, DivisionImage
@admin.register(DivisionImage)
class DivisionImageAdmin(admin.ModelAdmin):
    list_display = ('division', 'caption', 'uploaded_at')
    search_fields = ('division__name', 'caption')

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'sector', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('updated_at',)

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at', 'is_handled')
    list_filter = ('is_handled',)
    readonly_fields = ('submitted_at',)