from django.db import transaction as tx
from django.apps import apps
from django.conf import settings

from monarch.users.connectors import google

from . import serializers
from . import token


def make_auth_response_data(user) -> dict:
    """
    Given a domain and user, creates data structure
    using python dict containing a representation
    of the logged user.
    """
    serializer = serializers.UserSerializer(user)
    data = dict(serializer.data)
    data["auth_token"] = token.get_token_for_user(user, "authentication")
    return data
