from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class TranslatorForm(forms.Form):
    text_input = forms.CharField(help_text="Input text that contains Chinese characters")

    def clean_text_input(self):
        data = self.cleaned_data['text_input']

        return data