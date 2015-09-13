from monarch.common.api import routers

router = routers.DefaultRouter(trailing_slash=False)

# monarch.users
from monarch.users.api import AuthViewSet
router.register(r"auth", AuthViewSet, base_name="auth")
