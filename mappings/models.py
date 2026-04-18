from django.db import models
from patients.models import Patient
from doctors.models import Doctor


class PatientDoctorMapping(models.Model):
    """Model representing the many-to-many relationship between patients and doctors."""

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='doctor_mappings',
        help_text='The patient being assigned a doctor.',
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='patient_mappings',
        help_text='The doctor assigned to the patient.',
    )
    assigned_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, default='')

    class Meta:
        db_table = 'patient_doctor_mappings'
        unique_together = ('patient', 'doctor')  # Prevent duplicate assignments
        ordering = ['-assigned_at']
        verbose_name = 'Patient-Doctor Mapping'
        verbose_name_plural = 'Patient-Doctor Mappings'

    def __str__(self):
        return f'{self.patient.name} -> Dr. {self.doctor.name}'
