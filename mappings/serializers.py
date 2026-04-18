from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer


class MappingSerializer(serializers.ModelSerializer):
    """Serializer for creating Patient-Doctor mappings."""

    class Meta:
        model = PatientDoctorMapping
        fields = ('id', 'patient', 'doctor', 'notes', 'assigned_at')
        read_only_fields = ('id', 'assigned_at')

    def validate(self, data):
        """Check that this patient-doctor pair is not already mapped."""
        patient = data.get('patient')
        doctor = data.get('doctor')

        if patient and doctor:
            if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
                raise serializers.ValidationError(
                    f'Doctor "{doctor.name}" is already assigned to patient "{patient.name}".'
                )
        return data


class MappingDetailSerializer(serializers.ModelSerializer):
    """Serializer for reading mappings with nested patient and doctor details."""

    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ('id', 'patient', 'doctor', 'notes', 'assigned_at')
        read_only_fields = ('id', 'assigned_at')
