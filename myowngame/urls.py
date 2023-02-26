from django import urls
from django.urls import include, path, re_path
from djoser.views import UserViewSet, TokenCreateView, TokenDestroyView
 
from . import views


urlpatterns = [
    path('register/', UserViewSet.as_view({'post': 'create'}), name="register"),
	path("login/", TokenCreateView.as_view(), name="login"),
    path("logout/", TokenDestroyView.as_view(), name="login"),
    path('profile/', UserViewSet.as_view({'get': 'me'}), name="register"),
    path('update/', UserViewSet.as_view({'post': 'perform_update'}), name="update"),
    path('delete/', UserViewSet.as_view({'post': 'destroy'}), name="delete"),
]