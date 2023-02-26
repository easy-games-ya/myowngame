from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.response import Response

from mog_api.permissions import AuthorOrReadonly
from myowngame.models import CategoryModel, QuestionModel
from .serializers import CategorySerializer, QuestionSerializer


class CategoryListApiView(ListAPIView):
    '''List categories'''
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (AuthorOrReadonly, )
    # queryset = CategoryModel.objects.all().prefetch_related('question')
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    # def get(self, request, format=None):
    #     content = {
    #         'user': str(request.user),
    #         'auth': str(request.auth),
    #     }
    #     return Response(content)


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
        pk = self.kwargs.get('pk')
        if not pk:
            return QuestionModel.objects.all().select_related('category')
        return QuestionModel.objects.filter(category_id=pk).select_related('category')


class QuestionDetailApiView(RetrieveAPIView):
    '''Detail question'''
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (AuthorOrReadonly, )
    queryset = QuestionModel.objects.all().select_related('category')
    serializer_class = QuestionSerializer
