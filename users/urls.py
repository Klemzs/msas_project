from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterView, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
        path('register/', RegisterView.as_view(), name = 'register'),
        path('', include(router.urls)),
        path('login/', TokenObtainPairView.as_view(), name = 'login'),
]
