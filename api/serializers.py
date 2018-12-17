from rest_framework import serializers
from questions.models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, required=False)
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Question
        fields = ("id", "title", "author", "text", "stars")

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("id", "author", "text", "question", "stars")