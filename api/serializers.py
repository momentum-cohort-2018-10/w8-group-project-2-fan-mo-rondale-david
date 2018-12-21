from questions.models import StarredItem, Question, User, Answer
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_link = serializers.HyperlinkedIdentityField(view_name='user-detail')
    user_question_link = serializers.HyperlinkedIdentityField(
        view_name='question-list-by-user'
    )
    user_answer_link = serializers.HyperlinkedIdentityField(
        view_name='answer-list-by-user'
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'is_staff',
            'user_link',
            'user_question_link',
            'user_answer_link'
            )


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
    object_id = serializers.IntegerField(read_only=True)
    content_type = serializers.SlugRelatedField(
        slug_field='model',
        read_only=True)

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
    answer_detail_link = serializers.HyperlinkedIdentityField(
        view_name='answer-detail')

    star_count = serializers.IntegerField(source='stars.count', read_only=True)
    star_list_link = serializers.HyperlinkedIdentityField(
        view_name='answer-star-list')

    class Meta:
        model = Answer
        fields = (
                    "id",
                    "question",
                    "text",
                    "author",
                    'star_count',
                    "created_at",
                    'answer_detail_link',
                    'star_list_link'
                )


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    question_detail_link = serializers.HyperlinkedIdentityField(
        view_name='question-detail')
    answer_list_link = serializers.HyperlinkedIdentityField(
        view_name='question-answer-list')
    star_list_link = serializers.HyperlinkedIdentityField(
        view_name='question-star-list')
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
                    'answer_count',
                    'star_count',
                    'question_detail_link',
                    'answer_list_link',
                    'star_list_link'

                  )

    def create(self, validated_data):
        return Question.objects.create(**validated_data)
