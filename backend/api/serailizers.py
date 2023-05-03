from rest_framework import serializers
from base.models import Prompt, User, Action


class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = "__all__"


class ActionSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = "__all__"


class UserSerailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
