import pytest

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from datetime import date, timedelta

from booking_app.models import Room, Reservation

@pytest.mark.api
@pytest.mark.filterwarnings("ignore:Converter 'drf_format_suffix' is already registered.")
@pytest.mark.django_db
class TestRoomAPI:
    def setup_method(self):
        self.client = APIClient()
        self.room_description = "Test room"
        self.room_price = 0
        self.room = Room.objects.create(describe=self.room_description, price=self.room_price)

        self.booking_starts = date.today()
        self.booking_ends = date.today() + timedelta(days=5)
        self.reservation = Reservation.objects.create(
            room=self.room,
            booking_starts=self.booking_starts,
            booking_ends=self.booking_ends
        )

    def test_create_room(self):
        assert self.reservation.id is not None
        assert self.reservation.room == self.room
        assert self.reservation.booking_starts == self.booking_starts

    def test_get_reservation(self):
        url = reverse("reservation-list")
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_get_reservation_detail(self):
        url = reverse("reservation-detail", kwargs={'pk': self.reservation.pk})
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK

    def test_update_reservation(self):
        url = reverse("reservation-detail", kwargs={'pk': self.reservation.pk})
        room = Room.objects.create(describe="Test room for UPDATE", price=999)
        test_data = {
                'room': room.id,
                'booking_starts': "2025-01-21",
                'booking_ends': "2025-03-21"
            }
        response = self.client.put(url, test_data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['booking_starts'] == test_data['booking_starts']
        assert response.data['booking_ends'] == test_data['booking_ends']

    def test_patch_room(self):
        url = reverse("reservation-detail", kwargs={'pk': self.reservation.pk})
        test_data = {
            'booking_starts': "2025-04-21"
        }
        response = self.client.patch(url, test_data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['booking_starts'] == test_data['booking_starts']

    def test_delete_room(self):
        url = reverse("reservation-detail", kwargs={'pk': self.reservation.pk})
        response = self.client.delete(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] is None

    def test_get_reservations_by_room(self):
        Reservation.objects.create(
            room=self.room,
            booking_starts=self.booking_starts,
            booking_ends=self.booking_ends
        )

        url = reverse("reservation-by-room-num", kwargs={'room_id': self.room.id})
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        for _ in response.data:
            assert _['room'] == self.room.id
        assert len(response.data) == 2
