from django.urls import path, re_path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', AccountsAPI.as_view(), name='accounts'),
    path('create/', CreateAccountAPI.as_view(), name='create_account'),
    path('info/<int:pk>', AccountInfoAPI.as_view(), name='account_info'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
