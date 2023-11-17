from django.contrib.auth import login
from .models import UserProfile, Education
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from .forms import RegistrationForm, LoginForm, UserProfileForm, EducationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View

class RegistrationView(CreateView):
    template_name = 'skillapp/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        UserProfile.objects.create(user=user)
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'skillapp/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('registration')

from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    next_page = 'login'

class ProfileView(View):
    template_name = 'skillapp/profile.html'

    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        edu_details = Education.objects.filter(user_profile=user_profile)
        form = UserProfileForm(instance=user_profile)

        context = {
            'user_profile': user_profile,
            'edu_details' : edu_details,
            'form': form,
        }

        return render(request, self.template_name, context)

class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'skillapp/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.userprofile

class UserEducationalUpdateView(UpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'skillapp/education_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        user_profile = self.request.user.userprofile
        return Education.objects.get(user_profile=user_profile)