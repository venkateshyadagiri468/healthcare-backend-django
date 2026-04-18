from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    """Serializer for the Doctor model."""

    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Doctor
        fields = (
            'id',
            'name',
            'specialization',
            'contact',
            'email',
            'experience_years',
            'created_by',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')

    def validate_contact(self, value):
        """Ensure contact is not empty."""
        if not value.strip():
            raise serializers.ValidationError('Contact number cannot be empty.')
        return value.strip()

    def validate_email(self, value):
        """Check uniqueness, excluding the current instance on update."""
        instance = self.instance
        qs = Doctor.objects.filter(email=value.lower())
        if instance:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise serializers.ValidationError('A doctor with this email already exists.')
        return value.lower()
