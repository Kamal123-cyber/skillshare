from django.urls import path
from .views import HomePage, SkillUserDetailView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('user-detail/<int:pk>/', SkillUserDetailView.as_view(), name='userdetail'),
]
