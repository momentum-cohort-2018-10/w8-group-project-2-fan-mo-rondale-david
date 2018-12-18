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
    # content_object = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = StarredItem
        fields = ('user', 'object_id')


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    stars = StarredItemSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('title', 'author', 'text', 'stars')
