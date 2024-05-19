from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenBlacklistView)
from .views import AccountView

urlpatterns = [
    path('', AccountView.as_view()),
    path('<int:pk>', AccountView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('refresh/blacklist/', TokenBlacklistView.as_view()),
]