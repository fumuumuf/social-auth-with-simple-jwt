from rest_framework_simplejwt.tokens import RefreshToken
from rest_social_auth.serializers import JWTSerializer, UserSerializer


class SimpleJWTSerializer(JWTSerializer):
    def get_token(self, user):
        # get Simple JWT Token
        refresh = RefreshToken.for_user(user)

        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

        return token


class UserSimpleJWTSerializer(SimpleJWTSerializer, UserSerializer):
    pass
