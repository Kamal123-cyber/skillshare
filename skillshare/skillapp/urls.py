from django.urls import path
from .views import RegistrationView, CustomLoginView, CustomLogoutView, ProfileView, UserProfileUpdateView, UserEducationalUpdateView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-update/', UserProfileUpdateView.as_view(), name='profile_update'),
    path('educational-update/', UserEducationalUpdateView.as_view(), name='educational_update'),
]
