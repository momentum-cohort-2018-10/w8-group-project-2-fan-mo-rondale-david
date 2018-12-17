from main.models import Question, Answer
from api.serializers import QuestionSerializer, AnswerSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.
class QuestionListCreateView(APIView):                                      #Shows list of all questions in API view
    def get(self, request):
        questions = Questions.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):                                                #Allows ability to create a question in API view
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)                             #Turns user data into question object
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

class QuestionRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):      #Allows user ability to retrieve and destroy only their questions
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return self.request.user.questions


class AnswerCreateview(APIView):                                            #Shows list of all answers in API view
    def get(self, request):
        answers = Answers.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

    def post(self, request):                                                #Allows ability to create an answer in API view
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)                             #Turns user data into answer object
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

class AnswerRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):        #Allows user ability to retrieve and destroy only their answers
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return self.request.user.answers