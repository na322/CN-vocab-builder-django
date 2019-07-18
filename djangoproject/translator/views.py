from django.shortcuts import render
from django.http import HttpResponse
from .models import InputHistory
from .translator import Translator
from .forms import TranslatorForm

def home(request):
    if request.method == 'POST':
        form = TranslatorForm(request.POST)
    
        if form.is_valid():
            tl = Translator(form.cleaned_data['text_input'])
            context = {
                'form': form,
                'input': tl.text_input,
                'desc': zip(tl.list_sim, tl.list_trad, tl.list_py, tl.list_def)
            }
            if request.user.is_authenticated:
                input_history = InputHistory(input_raw=tl.text_input, user=request.user)
                input_history.save()
            return render(request, 'translator/home.html', context)
    else:
        form = TranslatorForm()
        context = {
            'form': form
        }
        return render(request, 'translator/home2.html', context)

def about(request):
    return render(request, 'translator/about.html')