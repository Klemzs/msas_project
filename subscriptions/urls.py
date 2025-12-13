from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import(
        SubscriptionViewSet,
        StartSubscriptionAPIView,
        RenewSubscriptionAPIView,
        CheckSubscriptionAPIView,
        )

router = DefaultRouter()
router.register(r'admin', SubscriptionViewSet, basename = 'subscription')

urlpatterns = [
        path('start/', StartSubscriptionAPIView.as_view(), name = 'start-subscription'),
        path('renew/', RenewSubscriptionAPIView.as_view(), name = 'renew-subscription'),
        path('check/', CheckSubscriptionAPIView.as_view(), name = 'check-subscription'),
        path('', include(router.urls)),
    ]
