from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.response import Response

from mog_api.permissions import AuthorOrReadonly
from myowngame.models import CategoryModel, QuestionModel
from .serializers import CategorySerializer, QuestionSerializer
from myowngame.models import CategoryModel


class CategoryListApiView(ListAPIView):
    """List category"""
    permission_classes = (AuthorOrReadonly, )
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        count = self.request.GET.get('count')
        if count is None:
            return CategoryModel.objects.all()
        return CategoryModel.objects.order_by('?')[:int(count)]
    

class CategoryDetailApiView(RetrieveAPIView):
    '''Detail categories'''
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (AuthorOrReadonly, )
    queryset = CategoryModel.objects.all().prefetch_related('question')
    serializer_class = CategorySerializer


class QuestionListApiView(ListAPIView):
    '''List question'''
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (AuthorOrReadonly, )
    serializer_class = QuestionSerializer
    def get_queryset(self):
        id_category = self.request.GET.get('category')
        if id_category is not None:
            category = get_object_or_404(CategoryModel, pk=id_category)
        score = self.request.GET.get('score')
        if score is None or category is None:
            return QuestionModel.objects.all().select_related('category')
        score = int(score)     
        # return QuestionModel.objects.order_by('?').filter(category_id=category.id, score=score).first()
        return QuestionModel.objects.order_by('?').filter(category=category, score=score)[0]


    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #     if not pk:
    #         return QuestionModel.objects.all().select_related('category')
    #     return QuestionModel.objects.filter(category_id=pk).select_related('category')


class QuestionDetailApiView(RetrieveAPIView):
    '''Detail question'''
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (AuthorOrReadonly, )
    queryset = QuestionModel.objects.all().select_related('category')
    serializer_class = QuestionSerializer
