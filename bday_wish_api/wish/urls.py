from django.urls import path
from .views import WishAPIView, WishDetails

urlpatterns = [
    path('api/wish/', WishAPIView.as_view()),
    path('api/detail/<int:id>', WishDetails.as_view())
]