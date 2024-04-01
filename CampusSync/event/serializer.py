from rest_framework import serializers
from .models import Event
from user.models import Host



class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        # fields = ['id', 'name', 'description', 'event_date'
        #           , 'date_posted',  'poster', 'host', 'upvotes', 'downvotes', 'saved_by']

        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    host = HostSerializer(many=False)
    class Meta:
        model = Event
        # fields = ['id', 'name', 'description', 'event_date'
        #           , 'date_posted',  'poster', 'host', 'upvotes', 'downvotes', 'saved_by']

        fields = '__all__'
