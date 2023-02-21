from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.response import Response

from myowngame.models import CategoryModel, QuestionModel
from .serializers import CategorySerializer, QuestionSerializer


class CategoryListApiView(ListAPIView):
    '''List categories'''
    authentication_classes = [SessionAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CategoryModel.objects.all().prefetch_related('question')
    serializer_class = CategorySerializer

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)


class CategoryDetailApiView(RetrieveAPIView):
    '''Detail categories'''
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CategoryModel.objects.all().prefetch_related('question')
    serializer_class = CategorySerializer


class QuestionListApiView(ListAPIView):
    '''List question'''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = QuestionSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return QuestionModel.objects.all().select_related('category')
        return QuestionModel.objects.filter(category_id=pk).select_related('category')


class QuestionDetailApiView(RetrieveAPIView):
    '''Detail question'''
    permission_classes = (permissions.IsAuthenticated,)
    queryset = QuestionModel.objects.all().select_related('category')
    serializer_class = QuestionSerializer
