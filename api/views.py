from api.serializers import (
    UserSerializer, StarredItemSerializer, QuestionSerializer,
    AnswerSerializer, ResolveSerializer, DetailedAnswerResolveSerializer)
from questions.models import User, StarredItem, Question, Answer, Resolve
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.permissions import (IsAuthorOrReadOnly, IsStarOwnerOrReadOnly,
                             IsAnswerOwnerOrReadOnly,
                             OnlyAuthorCanMarkResolved)
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)
from django.contrib.contenttypes.models import ContentType
from questions.notify import Notify


@api_view([
    'GET',
])
def api_root(request, format=None):
    return Response({
        'users':
        reverse('user-list', request=request, format=format),
        'questions':
        reverse('question-list', request=request, format=format),
        'my-questions':
        reverse('user-question-list', request=request, format=format),
        'my-answers':
        reverse('user-answer-list', request=request, format=format)
    })


class UserListView(generics.ListAPIView):
    """
    Retrieves list of all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """
    Detail page for a single user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserQuestionListView(generics.ListAPIView):
    """
    Retrieves author's list of questions
    """
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return Question.objects.filter(author=user)


class UserAnswerListView(generics.ListAPIView):
    """
    Retrieves author's list of answers
    """
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return Answer.objects.filter(author=user)


class StarredItemDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieves details of starred item
    Only owners and remove their stars
    TODO = make it specific for a logged in user
    """
    queryset = StarredItem.objects.all()
    serializer_class = StarredItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsStarOwnerOrReadOnly)


class QuestionListView(generics.ListCreateAPIView):
    """
    Retrieves list of questions
    Allows logged in users to submit new questions
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class QuestionDetailView(generics.RetrieveDestroyAPIView):
    """
    Retrieves details of one question
    Allows only authors to destroy their questions
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    )


class QuestionsByUserListView(generics.ListAPIView):
    """
    Retrieves list of questions by selected user
    """
    serializer_class = QuestionSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        user = User.objects.get(pk=pk)
        return Question.objects.filter(author=user)


class AnswersByUserListView(generics.ListAPIView):
    """
    Retrieves list of answers by selected user
    """
    serializer_class = AnswerSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        user = User.objects.get(pk=pk)
        return Answer.objects.filter(author=user)


class AnswerDetailView(generics.RetrieveDestroyAPIView):
    """
    Retrieves details for a specific answer
    Allows answer owners to delete
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAnswerOwnerOrReadOnly)


class QuestionAnswerList(generics.ListCreateAPIView):
    """
    Lists answers for a specific question
    Allows logged in users to post an answer
    """
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        question = Question.objects.get(pk=self.kwargs['pk'])
        return Answer.objects.filter(question=question)

    def perform_create(self, serializer):
        question = Question.objects.get(pk=self.kwargs['pk'])
        serializer.save(author=self.request.user, question=question)
        yag = Notify()
        to = question.author.email
        if to:
            subject = "QuestionBox answer alert!"
            content = self.request.user.username + " just gave an " \
                "answer to your question '" + question.title + "'"
            yag.sendemail(to, subject, content)


class QuestionStarList(generics.ListCreateAPIView):
    """
    Lists star instances for a specific question
    Allows logged in users to add a star
    """
    serializer_class = StarredItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        content_type = ContentType.objects.get(model='question')
        return StarredItem.objects.filter(
            object_id=self.kwargs['pk'], content_type=content_type)

    def perform_create(self, serializer):
        question = Question.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, content_object=question)


class QuestionResolve(generics.ListCreateAPIView):
    """
    Displays resolution for a question
    Allows question owner to choose a correct answer
    """
    permission_classes = (IsAuthenticatedOrReadOnly, OnlyAuthorCanMarkResolved)

    def get_queryset(self):
        question = Question.objects.get(pk=self.kwargs['pk'])
        return Resolve.objects.filter(resolved_question=question)

    def perform_create(self, serializer):
        question = Question.objects.get(pk=self.kwargs['pk'])
        serializer.save(resolved_question=question)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DetailedAnswerResolveSerializer
        if self.request.method == 'POST':
            return ResolveSerializer
        return ResolveSerializer


class AnswerStarList(generics.ListCreateAPIView):
    """
    Retrieves list of stars for an answer
    Allows logged in users to star an answer
    """
    serializer_class = StarredItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        content_type = ContentType.objects.get(model='answer')
        return StarredItem.objects.filter(
            object_id=self.kwargs['pk'], content_type=content_type)
        return StarredItem.objects.filter(
            object_id=self.kwargs['pk'], content_type=content_type)

    def perform_create(self, serializer):
        answer = Answer.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, content_object=answer)
