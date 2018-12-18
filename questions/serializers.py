from questions.models import StarredItem, Question, User, Answer
from rest_framework import serializers


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

    star_link = serializers.HyperlinkedIdentityField(view_name='star-detail')
    # content_object = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = StarredItem
        fields = ('user', 'object_id', 'content_type', 'star_link')

    def create(self, validated_data):
        return StarredItem.objects.create(**validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    stars = StarredItemSerializer(many=True, read_only=True)
    question_link = serializers.HyperlinkedIdentityField(
        view_name='question-detail')

    class Meta:
        model = Question
        fields = ('title', 'author', 'text', 'stars', 'question_link')

    def create(self, validated_data):
        return Question.objects.create(**validated_data)
