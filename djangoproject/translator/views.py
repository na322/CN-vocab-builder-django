from django.shortcuts import render
from django.http import HttpResponse
from .models import InputHistory
from .translator import Translator
from .forms import TranslatorForm

def home(request):
    context = {
        'form': None,
        'input': None,
        'res': None,
    }
    if request.method == 'POST':
        form = context['form'] = TranslatorForm(request.POST)
        if form.is_valid():
            tl = Translator(form.cleaned_data['text_input'])
            context['input'] = tl.text_input
            context['res'] = zip(tl.list_sim, tl.list_trad, tl.list_py, tl.list_def)
            if request.user.is_authenticated:
                input_history = InputHistory(input_raw=tl.text_input, user=request.user)
                input_history.save()
            return render(request, 'translator/home.html', context)
        else:
            return render(request, 'translator/home.html', context)
    else:
        context['form'] = TranslatorForm()
        return render(request, 'translator/home.html', context)

def about(request):
    return render(request, 'translator/about.html')