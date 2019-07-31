from rest_framework import serializers
from .models import InputHistory, UserVocabulary

class IHSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputHistory
        fields = ['input_raw', 'date_input']

class UVSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVocabulary
        fields = '__all__'