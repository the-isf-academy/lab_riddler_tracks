from django import forms
from .models import Riddle

class NewRiddleForm(forms.ModelForm):
    class Meta:
        model = Riddle
        fields = [
            'question', 
            'answer',
            'difficulty']

    
class GuessRiddleForm(forms.Form):
    guess = forms.CharField()