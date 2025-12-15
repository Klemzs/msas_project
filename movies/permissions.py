from rest_framework.pemissions import BasePermission
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
