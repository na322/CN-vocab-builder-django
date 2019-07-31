from .models import InputHistory, UserVocabulary, models_save
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import IHSerializer, UVSerializer
from .vocab_builder import CNVocabBuilder
# from .views import models_save

class VocabBuilderViewSet(viewsets.ViewSet):
    """
    to be done: implement viewset for api
    """
    # temporary basic authentication

    @action(detail=False, methods =['post'])
    def build(self, request, pk=None):
        vb = CNVocabBuilder(request.data)
        if request.user.is_authenticated:
            models_save(request, vb)
        return Response(vb.__dict__)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def history(self, request, pk=None):
        if request.method == 'GET':
            input_history = InputHistory.objects.values('input_raw', 'date_input', 'id').filter(user=request.user)
            serializer = IHSerializer(input_history, many=True, partial=True)
            return Response(serializer.data)

    @action(detail=False, methods =['get'], permission_classes=[IsAuthenticated])
    def vocab(self, request, pk=None):
        if request.method == 'GET':
            user_vocab = UserVocabulary.objects.values('phrase', 'input_history_id').filter(user=request.user)
            serializer = UVSerializer(user_vocab, many=True, partial=True)
            return Response(serializer.data)

