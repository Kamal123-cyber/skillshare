from django import forms
from .models import UserProfile, Education
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'profile_picture', 'skills_offered', 'age', 'religion', 'gender']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution_name', 'degree', 'field_of_study', 'graduation_year', 'achievements', 'teaching_experience']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']