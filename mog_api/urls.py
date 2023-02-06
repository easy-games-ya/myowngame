from django.conf.urls import url
from django.urls import path, include
from .views import (
    CategoryListApiView,
    CategoryDetailApiView,
    QuestionListApiView,
    QuestionDetailApiView,
)

urlpatterns = [
    path('api/category', CategoryListApiView.as_view()),
    path('api/category/<int:category_id>/', CategoryDetailApiView.as_view()),
    path('api/category/<int:category_id>/question', QuestionListApiView.as_view()),
    path('api/category/<int:category_id>/question/<int:question_id>/', QuestionDetailApiView.as_view()),
]