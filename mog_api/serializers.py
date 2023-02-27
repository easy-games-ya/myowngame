from rest_framework import serializers
from myowngame.models import CategoryModel, QuestionModel


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionModel
        fields = ["id", "question", "answer", "image", "category", "score"]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        # fields = ["id", "title", "description", "question"]
        fields = ["id", "title", "description"]

