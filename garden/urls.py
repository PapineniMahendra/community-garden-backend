from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, CommentViewSet, ParticipationViewSet, UserProfileView

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'participations', ParticipationViewSet, basename='participation')

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
