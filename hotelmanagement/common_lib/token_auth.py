import datetime
# import pytz
from django.conf import settings
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token

class ExpiringTokenAuthentication(TokenAuthentication):
    """
    Expiring token for mobile and desktop clients.
    It expires every {n} hrs requiring client to supply valid username 
    and password for new one to be created.
    """

    model = Token

    def authenticate_credentials(self, key, request=None):
        models = self.get_model()

        try:
            token = models.objects.select_related("user").get(key=key)
        except models.DoesNotExist:
            raise AuthenticationFailed(
                {"error": "Invalid or Inactive Token", "is_authenticated": False}
            )

        if not token.user.is_active:
            raise AuthenticationFailed(
                {"error": "Invalid user", "is_authenticated": False}
            )

        time_difference = (datetime.datetime.now() - token.created).total_seconds() / 60.0
        if time_difference > settings.TOKEN_TTL_MINTS:
            print('token expired')
            raise AuthenticationFailed(
                {"error": "Token has expired", "is_authenticated": False}
            )
        token.created = datetime.datetime.now()
        token.save()
        return token.user, token

