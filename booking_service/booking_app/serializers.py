from rest_framework import serializers

from .models import Room, Reservation

class RoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'describe', 'price']

class ReservationModelSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    booking_starts = serializers.DateField(format='%Y-%m-%d')
    booking_ends = serializers.DateField(format='%Y-%m-%d')
    class Meta:
        model = Reservation
        fields = ['id', 'room', 'booking_starts', 'booking_ends']
