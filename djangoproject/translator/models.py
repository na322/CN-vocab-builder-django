from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class InputHistory(models.Model):
    input_raw = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_input = models.DateTimeField(default=timezone.now)