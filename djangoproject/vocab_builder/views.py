from django.shortcuts import render
from django.http import HttpResponse
from .models import InputHistory, UserVocabulary
from .vocab_builder import CNVocabBuilder
from .forms import TextInputForm
from rest_framework.decorators import api_view
from rest_framework.response import Response

def home(request):
    context = {
        'form': None,
        'input': None,
        'res': None,
    }
    if request.method == 'POST':
        form = context['form'] = TextInputForm(request.POST)
        if form.is_valid():
            vb = CNVocabBuilder(form.cleaned_data['text_input'])
            context['input'] = vb.text_input
            context['res'] = zip(vb.list_sim, vb.list_trad, vb.list_py, vb.list_defi)
            if request.user.is_authenticated:
                input_history = InputHistory(input_raw=vb.text_input, user=request.user)
                input_history.save()
                for p in vb.list_sim:
                    user_vocab = UserVocabulary(phrase=p, user=request.user)
                    user_vocab.save()               
            return render(request, 'vocab_builder/home.html', context)
        else:
            return render(request, 'vocab_builder/home.html', context)
    else:
        context['form'] = TextInputForm()
        return render(request, 'vocab_builder/home.html', context)

def about(request):
    return render(request, 'vocab_builder/about.html')

@api_view(['POST'])
def api_build(request):
    if request.method == 'POST':
        vb = CNVocabBuilder(request.data)
        return HttpResponse(vb.jsonify_attributes())