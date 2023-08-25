from rest_framework import serializers
from .models import Objects
class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objects
        fields = ('lantitude', 'longitude', 'types', 'name')