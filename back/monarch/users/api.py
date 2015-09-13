from monarch.common.api import viewsets
from monarch.common import exceptions as exc
from monarch.common import responses as res

from . import services


class AuthViewSet(viewsets.GenericViewSet):
    # Login/Register view: /api/v1/users/auth
    def create(self, request, **kwargs):
        login_type = request.DATA.get("type", None)

        if login_type == "google":
            data = services.google_login(request)
            return res.Ok(data)

        raise exc.BadRequest(_("invalid login type"))
