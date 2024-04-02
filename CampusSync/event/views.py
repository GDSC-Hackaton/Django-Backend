from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.http import Http404, JsonResponse
from user.models import Host
from .serializer import EventSerializer
from .models import Event
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
 
class EventViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
