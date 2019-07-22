from django.shortcuts import render
from django.http import HttpResponse
from .models import InputHistory, UserVocabulary
from .vocab_builder import CNVocabBuilder
from .forms import TextInputForm

def home(request):
    context = {
        'form': None,
        'input': None,
        'res': None,
    }
    if request.method == 'POST':
        form = context['form'] = TextInputForm(request.POST)
        if form.is_valid():
            tl = CNVocabBuilder(form.cleaned_data['text_input'])
            context['input'] = tl.text_input
            context['res'] = zip(tl.list_sim, tl.list_trad, tl.list_py, tl.list_defi)
            if request.user.is_authenticated:
                input_history = InputHistory(input_raw=tl.text_input, user=request.user)
                input_history.save()
                for p in tl.list_sim:
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