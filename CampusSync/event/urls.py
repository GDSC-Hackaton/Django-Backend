from .views import EventViewSet, event_notifications, search, order_by_old, order_by_downvote,order_by_recent,order_by_upvote
from rest_framework.routers import DefaultRouter
from django.urls import path


router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
urlpatterns = router.urls + [
    path('event-notifications/', event_notifications),
    path('event-search/', search),
    path('event-order-recent/', order_by_recent),
    path('event-order-upvote/', order_by_upvote),
    path('event-order-downvote/', order_by_downvote),
    path('event-order-old/', order_by_old),
]

 