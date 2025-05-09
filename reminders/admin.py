from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'reminder_date', 'reminder_time', 'notification_method', 'status')
    list_filter = ('status', 'notification_method', 'reminder_date')
    search_fields = ('title', 'message', 'recipient')
    date_hierarchy = 'reminder_date'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'message')
        }),
        ('Reminder Details', {
            'fields': ('reminder_date', 'reminder_time', 'notification_method', 'recipient')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
