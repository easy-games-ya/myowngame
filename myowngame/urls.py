from django import urls
from django.urls import include, path, re_path
from . import views


urlpatterns = [
    # Login
    # path('login/', views.LoginView.as_view()),
    # path('logout/', views.LogoutView.as_view()),
    # path('profile/', views.ProfileView.as_view()),
    # path('register/', views.RegisterView.as_view(), name='auth_register'),
    # re_path(r'^auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]