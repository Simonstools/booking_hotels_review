# EasyB

## Hotel rooms booking web API
**For academic purpose only**

Supporting features:
- Full CRUD operations for room
- Full CRUD operations for booking entries
- Loading all bookings belong to certain room

**Installation**
1. Clone repo
```commandline
git clone https://github.com/Simonstools/booking_hotels.git
```
2. Change current directory
```commandline
cd booking_hotels
```
3. Setup .env file relying on .envexample, but it does not require. App will be launched properly with current settings in .envexample file, if changes will not be perfomed then just rename .envexample to .env.
```commandline
mv .envexample .env
```
4. Build and run application
```commandline
docker-compose up --build -d
```

**API endpoints**

```
/api/rooms/
/api/rooms/{room_id}/
/api/reservations/{reservation_id}/
/api/reservations/by_room/{room_id}
```

**Testing**

*Before run tests, set DB_HOST=localhost in .env file*