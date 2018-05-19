from django.conf.urls import url
from social_auth_jwt.views import SocialSimpleJWTOnlyAuthView,SocialSimpleJWTUserAuthView

urlpatterns = [
    url(r'^social/jwt/(?:(?P<provider>[a-zA-Z0-9_-]+)/?)?$',
        SocialSimpleJWTOnlyAuthView.as_view(),
        name='login_social_jwt'),

    # returns jwt + user_data
    url(r'^social/jwt_user/(?:(?P<provider>[a-zA-Z0-9_-]+)/?)?$',
        SocialSimpleJWTUserAuthView.as_view(),
        name='login_social_jwt_user'),
]
