from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from .serializers import RegisterSerializer,UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)
        refresh = str(refresh)

        headers = self.get_success_headers(serializer.data)
        return Response({
            "message": "Account created successfully",
            "refresh": refresh,
            "access": access,
            "user": UserSerializer(user).data
        }, status=status.HTTP_201_CREATED, headers=headers)

class UserViewSet(viewsets.ModelViewSet):
    """
    Admin can list/delete any user.
    Non-staff users can only retrieve/update their own account.
    Registration handled by RegisterView.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [permissions.AllowAny()]
        if self.action in ['list', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return User.objects.all()
        # Normal users only see themselves
        return User.objects.filter(id=user.id)
