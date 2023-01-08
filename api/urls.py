from django.urls import path
from .views import KitobAPIView

urlpatterns = [
    path('', KitobAPIView.as_view())
]
