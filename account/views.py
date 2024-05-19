from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from account.models import User
from django.shortcuts import get_object_or_404
from account.serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class AccountView(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
            return super().get_permissions()
        else:
            self.permission_classes = [AllowAny]
            return super().get_permissions()

    def get(self, request, pk):
        if request.user.id != pk:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = AccountSerializer(get_object_or_404(User, pk=pk))
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
