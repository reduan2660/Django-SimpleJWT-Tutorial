from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .api import *

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', user_profile.as_view(), name="user_profile"),
    path('register/', register.as_view(), name="user_registration"),
    path('reset/', change_password, name="change_password")
]