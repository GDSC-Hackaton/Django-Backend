from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
# from django.shortcuts import render, HttpResponse
from .serializer import EventSerializer
from .models import Event
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response


# Create your views here.
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def create_event(request):
    serializer = EventSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    print({'data': request.data})
    return JsonResponse( serializer.data )


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return JsonResponse( {'events': serializer.data} )

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def delete_event(request):
    event_id = request.data['id']
    event = Event.objects.filter(pk=int(event_id))
    if event:
        # event.delete()
        return JsonResponse({'status': 'succ'})
    return JsonResponse({'status': 'Err'})

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def update_event(request):
    
    event = Event.objects.get(pk=int(request.data['id']))
    serializer = EventSerializer(event, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse( {'events': "succ"} )
    return Response(serializer.errors)
    

def display_events(request):
    return render(request, "event/home.html")

def vote_event(request, event_id):
    # Write the vote logic here
    return redirect('')

def show_detail(request, event_id):
    # When a user click on the event this function will direct the user to the event detail page
    context = {"event_id" : event_id}
    return render(request, "event/home.html", context)


def search_event(request):
    # Here we are going to have a searched value with POST method to filter the objects by event name
    return render(request, "event/home.html", context)

def filter_event(request):
    # Again here the variable by holds the post value from the filter buttons
    context = {"events" : events}
    return render(request, "event/home.html", context)
