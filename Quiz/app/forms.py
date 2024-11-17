from django import forms
from .models import Question,UserAnswer,Choice
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'text','is_correct']

class UserAnswerForms(forms.ModelForm):
    class Meta:
        model = UserAnswer
        fields = ['user','question','selected_choice']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    