from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from myowngame.models import CategoryModel, QuestionModel
from .serializers import CategorySerializer, QuestionSerializer, QuestionFullSerializer
# Create your views here.


class CategoryListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]


    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the categories for given requested user
        '''
        # categories = CategoryModel.objects.filter(category=request.user.id)
        categories = CategoryModel.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    # def post(self, request, *args, **kwargs):
    #     '''
    #     Create the Todo with given todo data
    #     '''
    #     data = {
    #         'task': request.data.get('task'),
    #         'completed': request.data.get('completed'),
    #         'user': request.user.id
    #     }
    #     serializer = CategorySerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, category_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return CategoryModel.objects.get(id=category_id)
        except CategoryModel.DoesNotExist:
            return None

    def get(self, request, category_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        category_instance = self.get_object(category_id)
        if not category_instance:
            return Response(
                {"res": "Object with category id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CategorySerializer(category_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, category_id, *args, **kwargs):
        '''
        List all the categories for given requested user
        '''
        # categories = CategoryModel.objects.filter(category=request.user.id)
        questions = QuestionModel.objects.filter(category=category_id)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, category_id, question_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return QuestionModel.objects.get(id=question_id, category=category_id)
        except QuestionModel.DoesNotExist:
            return None

    def get(self, request, category_id, question_id,  *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        question_instance = self.get_object(category_id, question_id)
        if not question_instance:
            return Response(
                {"res": "Object with question id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = QuestionFullSerializer(question_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)