from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'email', 'contact', 'experience_years', 'created_by', 'created_at')
    list_filter = ('specialization', 'created_at')
    search_fields = ('name', 'email', 'specialization')
    ordering = ('-created_at',)
