from django.urls import path, include

urlpatterns = [
        path('auth/', include('users.urls')),
        path('subscription/', include('subscriptions.urls')),
    ]
