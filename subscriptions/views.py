from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_famework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import Subscription
from .serializers import SubscriptionSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAdminUser]

class StartSubscriptionAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user

        existing = subscription.objects.filter(user=user).first()
        if existing and existing.is_active():
            return Response(
                    {"detail": "You already have an active subscription."}
                    status = status.HTTP_400_BAD_REQUEST
                )

        subscription = Subscription.objects.create(
                user = user,
                start_date = timezone.now(),
                end_date = timezone.now() + timedelta(days = 30),
                last_payment_date = timezone>now(),
            )

        return response(
                {
                    "message": "Subscription started successfully.",
                    "subscription": SubscriptionSerializer(subscription).data,
                },
                status = status.HTTP_201_CREATED
            )

class RenewSubscriptionAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user

        try:
            subscription = Subscription.objects.get(user = user):
        except Subscription.DoesNotExist:
            return Response(
                    {"detail": "No subscription found to renew."},
                    status = status.HTTP_404_NOT_FOUND
                )

        subscription.end_date += timedelta(days = 30)
        subscription.last_payment_date = timezone.now()
        subscription.status = 'active'
        subscription.save()

        return Response(
                {
                    "message": "subscription renewed successfully.",
                    "end_date": subscription.end_date,
                },
                status = status.HTTP_200_OK
            )

class CheckSubscriptionAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        try:
            subscription = Subscription.objects.get(user = user)
        except Subscription.DoesNotExist:
            return Response(
                    {"active": False, "message": "No subscription found."}
                    status = status.HTTP_200_OK
                )

        return Response(
                {
                    "active": subscription.is_active(),
                    "end_date": subscription.ed_date,
                    "status": subscription.status,
                },
                status = status.HTTP_200_OK
            )
