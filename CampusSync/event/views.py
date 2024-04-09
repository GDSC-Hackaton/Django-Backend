from django.shortcuts import render
from rest_framework.response import Response
from .serializer import EventSerializer
from .models import Event
# from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema, OpenApiExample, inline_serializer

from rest_framework import status


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
    

@api_view(['GET'])
def order_by_recent(request):
    if request.method != 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    events = Event.objects.order_by("-recent")
    return Response(events.values())

@api_view(['GET'])
def order_by_old(request):
    if request.method != 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    events = Event.objects.order_by("recent")
    return Response(events.values())


@api_view(['GET'])
def order_by_upvote(request):
    if request.method != 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    events = Event.objects.order_by("-upvote")
    return Response(events.values())

@api_view(['GET'])
def order_by_downvote(request):
    if request.method != 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    events = Event.objects.order_by("-downvote")
    return Response(events.values())




def custom_404(request, exception):
    print("$$")
    return render(request, 'event/404.html', status=404)



@api_view(['GET'])
def search(request):
    if request.method != 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    #assuming the search-bar is event name 
    if 'event_name' not in request.data:
        return Response({'error': 'Missing required field: event_name'}, status=status.HTTP_400_BAD_REQUEST)

    event_name = request.data['event_name']
    events = Event.objects.filter(name__icontains=event_name)

    if not events.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Return the list of events
    return Response(events.values()) 




