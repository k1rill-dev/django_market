from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *


class UserSerializers(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Profile
        exclude = ('password', 'is_superuser', 'groups', 'user_permissions')

    def create(self, validated_data):
        user = Profile.objects.create(**validated_data)
        return user
