from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterView, UserViewSet, LoginView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
        path('register/', RegisterView.as_view(), name = 'register'),
        path('', include(router.urls)),
        path('login/', LoginView.as_view(), name = 'login'),
]
