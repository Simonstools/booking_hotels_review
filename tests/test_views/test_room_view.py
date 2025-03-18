import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from booking_app.models import Room

@pytest.mark.api
@pytest.mark.filterwarnings("ignore:Converter 'drf_format_suffix' is already registered.")
@pytest.mark.django_db
class TestRoomAPI:
    def setup_method(self):
        self.client = APIClient()
        self.room_description = "Test room"
        self.room_price = 0
        self.room = Room.objects.create(describe=self.room_description, price=self.room_price)

    def test_create_room(self):
        assert self.room.id is not None
        assert self.room.describe == self.room_description
        assert self.room.price == self.room_price

    def test_get_rooms(self):
        url = reverse("room-list")
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_get_room_detail(self):
        url = reverse("room-detail",kwargs={'pk': self.room.pk})
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK

    def test_update_room(self):
        url = reverse("room-detail", kwargs={'pk': self.room.pk})
        test_data = {
                'describe': "Test room PUT",
                'price': 1000
            }
        response = self.client.put(url, test_data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['describe'] == test_data['describe']
        assert response.data['price'] == test_data['price']

    def test_patch_room(self):
        url = reverse("room-detail", kwargs={'pk': self.room.pk})
        test_data = {
            'describe': "Test room PATCH"
        }
        response = self.client.patch(url, test_data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['describe'] == test_data['describe']

    def test_delete_room(self):
        url = reverse("room-detail", kwargs={'pk': self.room.pk})
        response = self.client.delete(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] is None
