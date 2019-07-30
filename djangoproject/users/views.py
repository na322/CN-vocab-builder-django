from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from vocab_builder.models import InputHistory, UserVocabulary

def context_factory(view_name):
    if view_name == 'register':
        return {'form': None}
    elif view_name == 'history':
        return {'input_history': None, 'user_vocab': None}


def register_get(request, context):
    context['form'] = UserRegisterForm()
    return render(request, 'users/register.html', context)

def register_post(request, context):
    form = context['form'] = UserRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account created with username: {username}')
        return redirect('login')

def register(request):
    context = context_factory('register')
    if request.method == 'POST': 
        return register_post(request, context)
    else: 
        return register_get(request, context)


@login_required
def history(request):
    context = context_factory(history)
    context['input_history'] = InputHistory.objects.values('input_raw', 'date_input').filter(user=request.user)
    context['user_vocab'] = UserVocabulary.objects.values('phrase').filter(user=request.user)
    return render(request, 'users/history.html', context)