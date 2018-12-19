from questions.models import StarredItem, Question, User, Answer
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_link = serializers.HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'user_link')


class StarredItemRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        if isinstance(value, Question):
            serializer = QuestionSerializer(value)
        elif isinstance(value, Answer):
            return 'Answer: ' + value.text
        else:
            raise Exception('Unexpected type of starred object.')

        return serializer.data


class StarredItemSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    content_type = serializers.SlugRelatedField(
        slug_field='model',
        queryset=ContentType.objects.filter(
            Q(model="question") | Q(model="answer")))

    star_link = serializers.HyperlinkedIdentityField(view_name='star-detail')

    class Meta:
        model = StarredItem
        fields = ('user', 'object_id', 'content_type', 'star_link')

    def create(self, validated_data):
        return StarredItem.objects.create(**validated_data)


class AnswerSerializer(serializers.ModelSerializer):
    """
    Add association to question to nest answers
    """
    author = serializers.StringRelatedField(read_only=True)
    question = serializers.PrimaryKeyRelatedField(read_only=True)
    answer_link = serializers.HyperlinkedIdentityField(
        view_name='answer-detail')

    star_count = serializers.IntegerField(source='stars.count', read_only=True)

    class Meta:
        model = Answer
        fields = (
                    "id",
                    "question",
                    "text",
                    "author",
                    'star_count',
                    "created_at",
                    'answer_link'
                )


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)
    question_link = serializers.HyperlinkedIdentityField(
        view_name='question-detail')
    answer_list_link = serializers.HyperlinkedIdentityField(
        view_name='question-answer-list')
    answer_count = serializers.IntegerField(source='answers.count', read_only=True)
    star_count = serializers.IntegerField(source='stars.count', read_only=True)

    class Meta:
        model = Question
        fields = (
                    'id',
                    'title',
                    'author',
                    'created_at',
                    'text',
                    'star_count',
                    'answers',
                    'answer_count',
                    'question_link',
                    'answer_list_link'
                    
                  )

    def create(self, validated_data):
        return Question.objects.create(**validated_data)
