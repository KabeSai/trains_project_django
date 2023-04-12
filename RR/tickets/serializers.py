from rest_framework import serializers
from .models import RoutePart, RailwayStation



class RailwayStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RailwayStation
        fields = ['name']

class TicketSerializer(serializers.ModelSerializer):
    start = RailwayStationSerializer()
    stop_uuid = RailwayStationSerializer()

    class Meta:
        model = RoutePart
        fields = ['start', 'stop_uuid', 'route_uuid', 'departure', 'arrival']

