from django.urls import path
from . import views


urlpatterns = [
    # Login
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('profile/', views.ProfileView.as_view()),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
]