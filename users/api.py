from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from .serializers import *

class user_profile(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        userId=self.request.user.id
        return User.objects.filter(id=userId)

class register(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User(phone=serializer.data['phone'])
        user.set_password(serializer.data['password'])
        user.save()

        return Response({'user': UserSerializer(user, context=self.get_serializer_context()).data,})

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def change_password(request):
     
    currentPassword = request.POST.get('oldPassword')
    newPassword = request.POST.get('newPassword')

    user_id = request.user.id
    user = User.objects.get(id=user_id)

    matchcheck= check_password(currentPassword, user.password)
    
    if matchcheck:
        user.set_password(newPassword)
        user.save()

        return Response({
            'success': True,
        }, status=200)
    
    else:
        return Response({
            'success': False,
            'error': 'Password Did not match'
        }, status=401)
