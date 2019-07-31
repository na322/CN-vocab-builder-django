from rest_framework import serializers
from .models import InputHistory, UserVocabulary

class IHSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputHistory
        fields = ['input_raw', 'date_input', 'user_id']

class UVSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVocabulary
        fields = ['phrase', 'input_history_id', 'user_id']