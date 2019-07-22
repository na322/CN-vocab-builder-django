from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from vocab_builder.models import InputHistory, UserVocabulary


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created with username: {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def history(request):
    input_history = InputHistory.objects.values('input_raw', 'date_input').filter(user=request.user)
    user_vocab = UserVocabulary.objects.filter(user=request.user)
    return render(request, 'users/history.html', {'input_history': input_history, 'user_vocab': user_vocab})