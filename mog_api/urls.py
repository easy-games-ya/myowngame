from django.urls import path

from .views import (
    CategoryListApiView,
    CategoryDetailApiView,
    QuestionListApiView,
    QuestionDetailApiView,
)

urlpatterns = [
    # List categories
    path('api/category/', CategoryListApiView.as_view()),
    # Detail category
    path('api/category/<int:pk>/', CategoryDetailApiView.as_view()),
    # List all questions
    path('api/question/', QuestionListApiView.as_view()),
    # List of questions by category
    path('api/question/category/<int:pk>/', QuestionListApiView.as_view()),
    # Detail question
    path('api/question/<int:pk>/', QuestionDetailApiView.as_view()),
]

