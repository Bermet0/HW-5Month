from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.RegistrationAPIView.as_view()),
    path('authorization/', views.AuthorizAPIView.as_view()),
    path('confirmation/', views.ConfirmAPIView.as_view()),
]
