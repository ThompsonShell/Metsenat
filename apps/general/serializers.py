from rest_framework import serializers
from .models import University


# USED by ModelSerializer
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"


# USED by Serializer
# class UniversitySerializer(serializers.Serializer):
#     def create(self, validate_data):
