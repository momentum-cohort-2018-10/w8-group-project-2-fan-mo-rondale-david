from questions.models import StarredItem, Question, User, Answer, Resolve
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


class ResolveAnswerField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        question = Question.objects.get(pk=self.self.kwargs['pk'])
        return Answer.objects.filter(question=question)


class ResolveSerializer(serializers.ModelSerializer):
    resolved_question = serializers.PrimaryKeyRelatedField(read_only=True)
    resolving_answer = serializers.PrimaryKeyRelatedField(
        queryset=Answer.objects.all())

    class Meta:
        model = Resolve
        fields = (
            'resolved_question',
            'resolving_answer'
        )

    def create(self, validated_data):
        return Resolve.objects.create(**validated_data)

    def __init__(self, *args, **kwargs):
        super(ResolveSerializer, self).__init__(*args, **kwargs)
        question = Question.objects.get(
            pk=self.context.get('request').parser_context['kwargs']['pk']
            )
        self.fields['resolving_answer'].queryset = Answer.objects.filter(
            question=question)


class StarredItemSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    object_id = serializers.IntegerField(read_only=True)
    content_type = serializers.SlugRelatedField(
        slug_field='model',
        read_only=True)

    star_link = serializers.HyperlinkedIdentityField(view_name='star-detail')

    class Meta:
        model = StarredItem
        fields = ('pk', 'user', 'object_id', 'content_type', 'star_link')

    def create(self, validated_data):
        return StarredItem.objects.create(**validated_data)


class AnswerSerializer(serializers.ModelSerializer):
    """
    Add association to question to nest answers
    """
    author = serializers.StringRelatedField(read_only=True)
    question = serializers.PrimaryKeyRelatedField(read_only=True)
    resolved_answer = serializers.BooleanField(read_only=True)
    starred = serializers.SerializerMethodField()
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
                    "starred",
                    "resolved_answer",
                    'star_count',
                    "created_at",
                    'answer_detail_link',
                    'star_list_link'
                )

    def get_starred(self, obj):
        answer = Answer.objects.get(pk=obj.pk)
        user = self.context.get('request').parser_context['request'].user
        user_star = answer.stars.filter(user=user)
        if user_star:
            return user_star[0].pk
        else:
            return 0


class DetailedAnswerResolveSerializer(serializers.ModelSerializer):
    resolved_question = serializers.PrimaryKeyRelatedField(read_only=True)
    resolving_answer = AnswerSerializer()

    class Meta:
        model = Resolve
        fields = (
            'resolved_question',
            'resolving_answer'
        )

    def create(self, validated_data):
        return Resolve.objects.create(**validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    starred = serializers.SerializerMethodField()
    resolved = DetailedAnswerResolveSerializer(read_only=True)

    question_resolution_link = serializers.HyperlinkedIdentityField(
        view_name='question-resolution'
    )
    question_detail_link = serializers.HyperlinkedIdentityField(
        view_name='question-detail')
    answer_list_link = serializers.HyperlinkedIdentityField(
        view_name='question-answer-list')
    star_list_link = serializers.HyperlinkedIdentityField(
        view_name='question-star-list')
    answer_count = serializers.IntegerField(source='answers.count',
                                            read_only=True)
    star_count = serializers.IntegerField(source='stars.count', read_only=True)

    class Meta:
        model = Question
        fields = (
                    'id',
                    'title',
                    'author',
                    'created_at',
                    'text',
                    'starred',
                    'resolved',
                    'answer_count',
                    'star_count',
                    'question_detail_link',
                    'question_resolution_link',
                    'answer_list_link',
                    'star_list_link'

                  )

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def get_starred(self, obj):
        question = Question.objects.get(pk=obj.pk)
        user = self.context.get('request').parser_context['request'].user
        user_star = question.stars.filter(user=user)
        if user_star:
            return user_star[0].pk
        else:
            return 0
