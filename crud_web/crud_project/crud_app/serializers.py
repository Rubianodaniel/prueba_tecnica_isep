from rest_framework import serializers
from .models import Validate

class ValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validate
        fields = '__all__'
