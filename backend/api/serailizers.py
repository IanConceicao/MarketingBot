from rest_framework import serializers
from base.models import Prompt, User, Action, Message


class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = "__all__"


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    actions = ActionSerializer(read_only=True, many=True)
    prompt = PromptSerializer(read_only=True)

    class Meta:
        model = Message
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = "__all__"
