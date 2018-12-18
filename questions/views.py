from django.shortcuts import render
from rest_framework import viewsets
from questions.serializers import (
    UserSerializer,
    StarredItemSerializer,
    QuestionSerializer)
from questions.models import User, StarredItem, Question
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from questions.permissions import IsAuthorOrReadOnly, IsStarOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'questions': reverse('question-list', request=request, format=format),
        'stars': reverse('star-list', request=request, format=format),
    })


def index(request):
    return render(request, 'index.html')


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StarredItemList(generics.ListCreateAPIView):
    queryset = StarredItem.objects.all()
    serializer_class = StarredItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StarredItemDetail(generics.RetrieveDestroyAPIView):
    queryset = StarredItem.objects.all()
    serializer_class = StarredItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsStarOwnerOrReadOnly)


class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class QuestionDetailView(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)
