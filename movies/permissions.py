from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.utils import timezone
from subscriptions.models import Subscription

class IsSubscribedUser(BasePermission):
    message = "You need an active subscription to watch this movie."

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        return Subscription.objects.filter(
                user = user,
                end_date__gte = timezone.now()
        ).exists()

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

