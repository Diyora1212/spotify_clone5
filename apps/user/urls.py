from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from apps.user.api_endpoints.Follow import (
    UserFollowView,
    UserUnfollowView,
    UserFollowersView,
    UserFollowingsView,
    UserArtistFollowView,
    UserArtistUnFollowView,
)
from apps.user.api_endpoints.User import UserCreateView, UserActivateView, ForgotPasswordAPIView, ResetPasswordView
from apps.user.views import MyCustomObtainTokenView

app_name = "user"

urlpatterns = [
    path("token/", MyCustomObtainTokenView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('register/', UserCreateView.as_view(), name="user-create"),
    path('user-activate/<str:token>', UserActivateView.as_view(), name="user-activate"),
    path('user-password-forget/<str:token>', ForgotPasswordAPIView.as_view(), name="forgot-password" ),
    path('user-password-reset/<str:token>', ResetPasswordView.as_view(), name="reset-password"),
    path("user-follow/", UserFollowView.as_view()),
    path("user-unfollow/", UserUnfollowView.as_view()),
    path("artist-follow/", UserArtistFollowView.as_view()),
    path("artist-unfollow/", UserArtistUnFollowView.as_view()),
    path("<pk>/followers/", UserFollowersView.as_view()),
    path("<pk>/followings/", UserFollowingsView.as_view()),
]
