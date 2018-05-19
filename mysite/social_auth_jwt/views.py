from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_social_auth.views import JWTAuthMixin, BaseSocialAuthView

from social_auth_jwt.serializer import SimpleJWTSerializer, UserSimpleJWTSerializer


class SocialSimpleJWTOnlyAuthView(JWTAuthMixin, BaseSocialAuthView):
    serializer_class = SimpleJWTSerializer


class SocialSimpleJWTUserAuthView(JWTAuthMixin, BaseSocialAuthView):
    serializer_class = UserSimpleJWTSerializer
