from rest_framework import serializers
from myowngame.models import CategoryModel, QuestionModel


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ["id", "score"]


class QuestionFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ["id", "question", "score", "score"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["id", "title", "description"]
        # embedded_fields = {"items": QuestionSerializer}
