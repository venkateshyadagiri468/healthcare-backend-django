from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    """Serializer for the Patient model."""

    created_by = serializers.StringRelatedField(read_only=True)

    doctors = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = (
            'id',
            'name',
            'age',
            'gender',
            'contact',
            'address',
            'medical_history',
            'created_by',
            'created_at',
            'updated_at',
            'doctors',
        )
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at', 'doctors')

    def get_doctors(self, obj):
        mappings = obj.doctor_mappings.select_related('doctor').all()
        return [
            {
                'id': mapping.doctor.id,
                'name': mapping.doctor.name,
                'specialization': mapping.doctor.specialization,
            }
            for mapping in mappings
        ]
    def validate_age(self, value):
        """Ensure age is a reasonable positive value."""
        if value <= 0 or value > 150:
            raise serializers.ValidationError('Age must be between 1 and 150.')
        return value

    def validate_contact(self, value):
        """Ensure contact number is not empty."""
        if not value.strip():
            raise serializers.ValidationError('Contact number cannot be empty.')
        return value.strip()
