from urllib.parse import parse_qs
from jwt import decode as jwt_decode

from django.conf import settings

from django.db import close_old_connections
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from channels.auth import AuthMiddlewareStack


class TokenAuthMiddleware:
    """
    Token authorization middleware for Django Channels 2
    """

    def __init__(self, inner):
        # Store the ASGI application we were passed
        self.inner = inner

    def __call__(self, scope):
        # Close old database connections to prevent usage of timed out connections
        close_old_connections()
        headers = dict(scope['headers'])
        if b'Token' in headers:
            # try:
            #     token_name, token_key = headers[b'token'].decode().split()
            #     if token_name == 'Token':
            #         token = Token.objects.get(key=token_key)
            #         scope['user'] = token.user
            #         # close_old_connections()
            # except Token.DoesNotExist:
            #     scope['user'] = AnonymousUser()
            token = headers[b'Token'].decode()
        else:
            # Get the token
            token = parse_qs(scope["query_string"].decode("utf8"))["token"][0]

        # Try to authenticate the user
        try:
            # This will automatically validate the token and raise an error if token is invalid
            UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            # Token is invalid
            # print(e)
            user = AnonymousUser()
        else:
            #  Then token is valid, decode it
            decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            # print(decoded_data)
            # Get the user using ID
            user = get_user_model().objects.get(id=decoded_data["user_id"])

        # Return the inner application directly and let it run everything else
        return self.inner(dict(scope, user=user))


TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))
