from .models import InputHistory, UserVocabulary
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import IHSerializer, UVSerializer
from .vocab_builder import CNVocabBuilder

class VocabBuilderViewSet(viewsets.ViewSet):
    """
    to be done: implement viewset for api
    """
    # temporary basic authentication
    # def get_permissions(self):
    #     if self.action == 'build':
    #         permission_classes = [AllowAny|IsAuthenticated]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]


    @action(detail=False, methods =['post'])
    def build(self, request, pk=None):
        vb = CNVocabBuilder(request.data)
        return Response(vb.__dict__)

    @action(detail=False, methods=['get', 'post'], permission_classes=[IsAuthenticated])
    def history(self, request, pk=None):
        if request.method == 'GET':
            input_history = InputHistory.objects.values('input_raw', 'date_input').filter(user=request.user)
            serializer = IHSerializer(input_history, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            # to do
            pass

    @action(detail=False, methods =['get', 'post'], permission_classes=[IsAuthenticated])
    def vocab(self, request, pk=None):
        if request.method == 'GET':
            user_vocab = UserVocabulary.objects.values('phrase').filter(user=request.user)
            serializer = UVSerializer(user_vocab, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            # to do
            pass

