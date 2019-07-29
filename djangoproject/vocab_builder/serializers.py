from rest_framework import serializers
from .models import InputHistory, UserVocabulary

class IHSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputHistory
        fields = '__all__'

class UVSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVocabulary
        fields = '__all__'