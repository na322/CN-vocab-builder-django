from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class InputHistory(models.Model):
    input_raw = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_input = models.DateTimeField(default=timezone.now)

    objects = models.Manager()

class UserVocabulary(models.Model):
    phrase = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_history = models.ForeignKey(InputHistory, on_delete=models.CASCADE)

    objects = models.Manager()

def models_save(request, vb):
    input_history = InputHistory(input_raw=vb.text_input, user=request.user)
    input_history.save()
    for p in vb.list_sim:
        user_vocab = UserVocabulary(phrase=p, user=request.user, input_history=input_history)
        user_vocab.save()        