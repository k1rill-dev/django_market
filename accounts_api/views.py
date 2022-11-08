from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, Http404
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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


class CreateAccountAPI(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializers

class AccountInfoAPI(RetrieveUpdateAPIView):
    # Allow only authenticated users to access this url
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializers

    def get(self, request, *args, **kwargs):
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        serializer = UserSerializers(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
