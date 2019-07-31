from .models import InputHistory, UserVocabulary
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import IHSerializer, UVSerializer
from .vocab_builder import CNVocabBuilder

class VocabBuilderViewSet(viewsets.ViewSet):
    """
    to be done: implement viewset for api
    """
    @action(detail=False, methods = ['post'])
    def build(self, request, pk=None):
        vb = CNVocabBuilder(request.data)
        return Response(vb.__dict__)

    @action(detail=False, methods = ['get', 'post'])
    def history(self, request, pk=None):
        if request.method == 'GET':
            input_history = InputHistory.objects.all()
            serializer = IHSerializer(input_history, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            # to do
            pass

    @action(detail=False, methods = ['get', 'post'])
    def vocab(self, request, pk=None):
        if request.method == 'GET':
            user_vocab = UserVocabulary.objects.all()
            serializer = UVSerializer(user_vocab, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            # to do
            pass

