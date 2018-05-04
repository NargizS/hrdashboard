from django import forms
from profiles.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

class DateInput(forms.DateInput):
    input_type = 'date'
    
class ProfileForm(forms.ModelForm):
    template_name='profile.html'
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'gender', 'city', 'date_of_birth', 'university', 'gpa', 'experience')
        widgets = {
            'date_of_birth': DateInput()
        }