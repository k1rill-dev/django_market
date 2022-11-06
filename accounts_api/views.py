from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *

class AccountsAPI(APIView):
    def get(self, request):

        accounts = Profile.objects.all()
        serializer = UserSerializers(accounts, many=True)

        return JsonResponse({
            'success': True,
            'accounts': serializer.data
        })
