from .models import InputHistory, UserVocabulary
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import IHSerializer, UVSerializer
from .vocab_builder import CNVocabBuilder

class VocabBuilderViewSet(viewsets.ViewSet):
    """
    """
    def build_vocab(self, request):
        pass
