from django.shortcuts import render
from rest_framework import viewsets
from questions.serializers import (
    UserSerializer,
    StarredItemSerializer,
    QuestionSerializer)
from questions.models import User, StarredItem, Question
from rest_framework import generics


def index(request):
    return render(request, 'index.html')


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StarredItemList(generics.ListAPIView):
    queryset = StarredItem.objects.all()
    serializer_class = StarredItemSerializer


class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
