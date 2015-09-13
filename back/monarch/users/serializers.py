from monarch.common.api import serializers

from  . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ("password",)

