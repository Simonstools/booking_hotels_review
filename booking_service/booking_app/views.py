from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework import status
from rest_framework.decorators import action

from .models import Room, Reservation
from .serializers import RoomModelSerializer, ReservationModelSerializer

class RoomAPIView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['price', 'time_create']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        room = serializer.save()
        output_data = {'room_id': room.id}
        return Response(data=output_data,
                        status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        room = self.get_object()
        serializer = self.get_serializer(room)
        self.perform_destroy(room)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)


class ReservationAPIView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationModelSerializer

    @action(detail=False, methods=['get'], url_path='by_room/(?P<room_id>[^/.]+)')
    def by_room_num(self, request, room_id=None):
        reservations = Reservation.objects.all().filter(room_id=room_id)
        serializer = self.get_serializer(reservations, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reservation = serializer.save()
        output_data = {'booking_id': reservation.id}
        return Response(data=output_data,
                        status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        reservation = self.get_object()
        serializer = self.get_serializer(reservation)
        self.perform_destroy(reservation)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)



