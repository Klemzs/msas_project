from rest_framework import serializers
from .models import Subscription
from django.utils import timezone
from datetime import timedelta

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'status', 'start_date', 'end_date', 'last_payment_date']
        read_only_fields = ['id', 'start_date', 'end_date', 'last_payment_date']
