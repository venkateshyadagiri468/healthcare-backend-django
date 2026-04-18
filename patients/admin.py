from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'contact', 'created_by', 'created_at')
    list_filter = ('gender', 'created_at')
    search_fields = ('name', 'contact', 'created_by__email')
    ordering = ('-created_at',)
