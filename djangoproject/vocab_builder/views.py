from django.shortcuts import render
from django.http import HttpResponse
from .models import InputHistory, UserVocabulary
from .vocab_builder import CNVocabBuilder
from .forms import TextInputForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import IHSerializer, UVSerializer

def models_save(request, vb):
    input_history = InputHistory(input_raw=vb.text_input, user=request.user)
    input_history.save()
    for p in vb.list_sim:
        user_vocab = UserVocabulary(phrase=p, user=request.user, input_history=input_history)
        user_vocab.save()               

def home_post(request, context):
    form = context['form']
    if form.is_valid():
        vb = CNVocabBuilder(form.cleaned_data['text_input'])
        context['input'] = vb.text_input
        context['res'] = zip(vb.list_sim, vb.list_trad, vb.list_py, vb.list_defi)
        if request.user.is_authenticated: models_save(request, vb)             
        return render(request, 'vocab_builder/home.html', context)
    else:
        return render(request, 'vocab_builder/home.html', context)

def home(request):
    context = {
        'form': None,
        'input': None,
        'res': None,
    }
    if request.method == 'POST':
        context['form'] = TextInputForm(request.POST)
        return home_post(request, context)
    else:
        context['form'] = TextInputForm()
        return render(request, 'vocab_builder/home.html', context)

def about(request):
    return render(request, 'vocab_builder/about.html')

@api_view(['POST'])
def api_build(request):
    vb = CNVocabBuilder(request.data)
    return Response(vb.__dict__)

@api_view(['GET', 'POST'])
def api_history(request):
    if request.method == 'GET':
        input_history = InputHistory.objects.all()
        serializer = IHSerializer(input_history, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        # to do
        pass

@api_view(['GET', 'POST'])
def api_vocab(request):
    if request.method == 'GET':
        user_vocab = UserVocabulary.objects.all()
        serializer = UVSerializer(user_vocab, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        # to do
        pass
    