from django.shortcuts import render
from django.http import HttpResponse
from .models import InputHistory, UserVocabulary
from .vocab_builder import CNVocabBuilder
from .forms import TextInputForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import IHSerializer, UVSerializer

def context_factory(view_name):
    if view_name == 'home':
        return {'form': None, 'input': None, 'res': None}


def models_save(request, vb):
    input_history = InputHistory(input_raw=vb.text_input, user=request.user)
    input_history.save()
    for p in vb.list_sim:
        user_vocab = UserVocabulary(phrase=p, user=request.user, input_history=input_history)
        user_vocab.save()               


def home_post(request, context):
    form = context['form'] = TextInputForm(request.POST)
    if form.is_valid():
        vb = CNVocabBuilder(form.cleaned_data['text_input'])
        context['input'] = vb.text_input
        context['res'] = zip(vb.list_sim, vb.list_trad, vb.list_py, vb.list_defi)
        if request.user.is_authenticated: 
            models_save(request, vb)             
    return render(request, 'vocab_builder/home.html', context)

def home_get(request, context):
    context['form'] = TextInputForm()
    return render(request, 'vocab_builder/home.html', context)

def home(request):
    context = context_factory('home')
    if request.method == 'POST':
        return home_post(request, context)
    else:
        return home_get(request, context)


def about(request):
    return render(request, 'vocab_builder/about.html')
    