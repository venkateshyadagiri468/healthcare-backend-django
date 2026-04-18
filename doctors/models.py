from django.db import models
from django.conf import settings


class Doctor(models.Model):
    """Model representing a doctor in the healthcare system."""

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='doctors',
        help_text='The user who added this doctor.',
    )
    name = models.CharField(max_length=150)
    specialization = models.CharField(max_length=150)
    contact = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    experience_years = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'doctors'
        ordering = ['-created_at']
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return f'Dr. {self.name} - {self.specialization}'
