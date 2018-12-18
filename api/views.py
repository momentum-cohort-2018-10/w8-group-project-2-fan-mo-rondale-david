from django.shortcuts import render
from questions.models import Question
from api.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def question_list(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)