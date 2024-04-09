from .views import EventViewSet, event_notifications
from rest_framework.routers import DefaultRouter
from django.urls import path


router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
urlpatterns = router.urls + [
    path('event-notifications/', event_notifications),
    path('events/<int:event_id>/upvote/', views.upvote_event, name='upvote_event'),
    path('events/<int:event_id>/downvote/', views.downvote_event, name='downvote_event')
]

 