from django.urls import path
from .views import public_view, protected_view, list_telegram_users

urlpatterns = [
    path('public/', public_view),
    path('protected/', protected_view),
    path('telegram-users/', list_telegram_users), 
]
