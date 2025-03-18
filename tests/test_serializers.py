import pytest
from datetime import date

from booking_app.serializers import (
    RoomModelSerializer,
    ReservationModelSerializer
)
from booking_app.models import Room, Reservation

@pytest.mark.django_db
class TestRoomSerializer:

    def test_valid_data(self):
        data = {'describe': 'Room test valid data in serialization', 'price': 100_000}
        serializer = RoomModelSerializer(data=data)

        assert serializer.is_valid()
        assert serializer.validated_data['describe'] == data['describe']
        assert serializer.validated_data['price'] == data['price']

    def test_serialization(self):
        test_data = {'describe': "Room test serialization", 'price': 200_000}
        room = Room.objects.create(describe=test_data['describe'], price=test_data['price'])

        serializer = RoomModelSerializer(instance=room)
        assert serializer.data == {
            'id': room.id,
            'describe': test_data['describe'],
            'price': test_data['price']
        }

    def test_deserialization(self):
        test_data = {'describe': "Room test serialization", 'price': 300_000}
        serializer = RoomModelSerializer(data=test_data)

        assert serializer.is_valid()
        room = serializer.save()
        assert room.describe == test_data['describe']
        assert room.price == test_data['price']

@pytest.mark.django_db
class TestReservationSerialization:

    def test_serialization(self):
        room = Room.objects.create(describe="Room test reserve serialization", price=0)
        data = {'room': room, 'booking_starts': "2025-02-22", 'booking_ends': "2025-08-22"}
        reservation = Reservation.objects.create(
            room=data['room'],
            booking_starts=data['booking_starts'],
            booking_ends=data['booking_ends']
        )

        serializer = ReservationModelSerializer(instance=reservation)

        print(serializer.data)

        assert serializer.data == {
            'id': reservation.id,
            'room': room.id,
            'booking_starts': data['booking_starts'],
            'booking_ends': data['booking_ends']
        }

    def test_deserialization(self):
        room = Room.objects.create(describe="Room test reserve deserialization", price=10)
        data = {'room': room.id, 'booking_starts': date.today(), 'booking_ends': date.today()}

        serializer = ReservationModelSerializer(data=data)
        assert serializer.is_valid()
        reservation = serializer.save()
        assert reservation.room == room
        assert reservation.booking_starts == data['booking_starts']
        assert reservation.booking_ends == data['booking_ends']
