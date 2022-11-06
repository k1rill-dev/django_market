from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', AccountsAPI.as_view(), name='accounts'),
]
