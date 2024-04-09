from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from rest_framework.response import Response
from .serializer import EventSerializer
from .models import Event


import mimetypes
from django.http import HttpResponse
# from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, OpenApiExample, inline_serializer
from rest_framework.permissions import IsAuthenticated


class EventViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

@api_view(['GET','POST']) 
def event_notifications(request):
    print(request.data)
    event_id = request.data['event_id']
    event = Event.objects.filter(pk=event_id)

    if request.method == 'GET' and event:
        return Response({'status': 'succesful get',
                        'event_id': str(event_id),
                        'event_notifications': str(event.notifications)})
    
    elif request.method == 'POST' and event:
        change = request.data[change]
        event.notifications = event.notifications + int(change)
        event.save()

        return Response({'status': 'succesful post',
                        'event_id': str(event_id),
                        'event_notifications': str(event.notifications)})
    
    return Response({'status': 'Failed, no such event'})


def custom_404(request, exception):
    print("$$")
    return render(request, 'event/404.html', status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upvote_event(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return Response({'error': 'Event not found'}, status=404)

    if request.method == 'POST':
        user = request.user
        if user in event.voters.all():
            return Response({'error': 'You have already upvoted this event'}, status=400)
        event.voters.add(user)
        event.upvotes = event.voters.count()
        event.save()

        return Response({'status': 'Upvoted successfully',
                         'event_id': event_id,
                         'upvotes': event.upvotes})
    else:
        return Response({'error': 'Invalid request method'}, status=405)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def downvote_event(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return Response({'error': 'Event not found'}, status=404)

    if request.method == 'POST':
        user = request.user
        if user in event.downvoters.all():
            return Response({'error': 'You have already downvoted this event'}, status=400)

        event.downvoters.add(user)
        event.downvotes = event.downvoters.count()
        event.save()

        return Response({'status': 'Downvoted successfully',
                         'event_id': event_id,
                         'downvotes': event.downvotes})
    else:
        return Response({'error': 'Invalid request method'}, status=405)