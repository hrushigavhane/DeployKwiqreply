from django.contrib.auth.tokens import PasswordResetTokenGenerator
import django.utils.six as six
from .models import User_Details


class TokenGenerator(PasswordResetTokenGenerator):
    user = User_Details()

    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp)
        )
account_activation_token = TokenGenerator()
