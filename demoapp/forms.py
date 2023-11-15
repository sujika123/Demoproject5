from django import forms
from django.contrib.auth.forms import UserCreationForm

from demoapp.models import Login, userlogin, addevent


class DateInput(forms.DateInput):
    input_type = "date"

GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female')
]

class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget = forms.PasswordInput,label = 'password')
    password2 = forms.CharField(widget = forms.PasswordInput, label = 'Confirm password')
    class Meta:
        model = Login
        fields = ('username','password1','password2')

class userloginform(forms.ModelForm):
    gender = forms.ChoiceField(widget = forms.RadioSelect,choices = GENDER_CHOICES)
    class Meta:
        model = userlogin
        fields = ('name','age','gender','address','phone','image')

class eventaddform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = addevent
        fields = ('name','date','description','image')
