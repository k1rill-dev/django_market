from rest_framework.serializers import ModelSerializer
from .models import *


class UserSerializers(ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('password', 'is_superuser', 'groups', 'user_permissions')
