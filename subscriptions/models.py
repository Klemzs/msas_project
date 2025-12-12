from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Create your models here.

def default_end_date():
    return timezone.now() + timedelta(days=30)

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.CharField(max_length = 20, default = 'active')
    start_date = models.DateTimeField(default = timezone.now)
    end_date = models.DateTimeField(default = default_end_date)
    last_payment_date = models.DateTimeField(default = timezone.now)

    def is_active(self):
        return self.end_date >= timezone.now()

    def __str__(self):
        return f"{self.user.username} - {self.status}"
