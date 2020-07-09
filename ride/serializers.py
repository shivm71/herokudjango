from rest_framework import serializers

from ride.models import Ride

class BookSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    start_x = serializers.CharField()
    start_y = serializers.CharField()
    end_x = serializers.CharField()
    end_y = serializers.CharField()


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        # exclude = ['id']
        fields = ['ride_id', 'ride_start_time', 'ride_end_time', 'start_x', 'start_y', 'end_x', 'end_y', 'driver',
                  'car', 'user_name', 'fare', 'status', 'distance', 'estimated_time']
        depth = 2
