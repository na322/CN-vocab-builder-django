from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .vocab_builder import CNVocabBuilder as cnvb
from .exceptions import ChineseCharsNotFound

class TextInputForm(forms.Form):
    text_input = forms.CharField(help_text="Input text that contains Chinese characters, press Enter to translate", label='', initial="我来到北京清华大学")

    def clean_text_input(self):
        data = self.cleaned_data['text_input']
        try:
            cnvb.check_text(data)
        except ChineseCharsNotFound as e:
            raise ValidationError(e.msg)
        return data