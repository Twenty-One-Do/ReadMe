from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenBlacklistView)
from . import views

urlpatterns = [
    path('', views.signup),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('refresh/blacklist/', TokenBlacklistView.as_view()),
]