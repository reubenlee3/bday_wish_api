from django.urls import path
from .views import (
    WishListView, 
    WishDetailView,
    WishSearchView,
)

urlpatterns = [
    path('api/list/', WishListView.as_view()),
    path('api/detail/<int:pk>', WishDetailView.as_view()),
    path('api/search/', WishSearchView.as_view()),
]