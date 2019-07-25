from rest_framework import serializers
from .models import InputHistory, UserVocabulary

class IHSerialiser(serializers.ModelSerializer):
    class Meta:
        model = InputHistory
        fields = '__all__'

class UVSerialiser(serializers.ModelSerializer):
    class Meta:
        model = UserVocabulary
        fields = '__all__'