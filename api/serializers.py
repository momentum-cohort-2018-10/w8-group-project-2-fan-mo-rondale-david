from rest_framework import serializers
from questions.models import Question, Answer

class AnswerSerializer(serializers.ModelSerializer):                        #Add association to question to nest answers
    author = serializers.StringRelatedField()
    class Meta:
        model = Answer
        fields = ("id", "question", "text", "author", "created_at")


class QuestionSerializer(serializers.ModelSerializer):
    # answers = AnswerSerializer(many=True)                                 #Answer needs to be associated to the question
    author = serializers.StringRelatedField()                               #Returns author as a string and not id
    class Meta:
        model = Question
        fields = ("id", "title", "text", "author", "created_at")
