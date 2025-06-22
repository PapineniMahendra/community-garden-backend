from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EventViewSet,
    CommentViewSet,
    ParticipationViewSet,
    UserProfileView,
    RegisterView,
)

# ✅ Initialize DRF Router
router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'participations', ParticipationViewSet, basename='participation')

# ✅ Define URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Event, Comment, Participation endpoints
    path('profile/', UserProfileView.as_view(), name='user-profile'),  # Profile view/update
    path('register/', RegisterView.as_view(), name='register'),  # User registration
]
