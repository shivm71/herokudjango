import math
from rest_framework.views import APIView
from .models import Car, Ride
from .serializers import RideSerializer
from rest_framework.response import Response


def get_distance(data):
    return round(math.sqrt((data["start_x"] - data["end_x"]) ** 2 + (data["start_y"] - data["end_y"]) ** 2),2)


def get_fare(data):
    base_cost = 20
    return round(base_cost + (get_distance(data) * 10),2)

def get_estimated_time(data):
    speed = 40
    return round(get_distance(data) / speed,2)


class Book(APIView):
    serializer_class = RideSerializer

    def post(self, request):
        data = request.data
        for key in data:
            if key != "user_name":
                data[key] = float(data[key])
                data[key] = float(data[key])

        car = self.get_nearest_car(data)
        response_return = self.book_ride(car, data)
        return Response(data = response_return,status=200)

    def book_ride(self, car, data):
        obj, created = Ride.objects.get_or_create(
            start_x=data["start_x"],
            start_y=data["start_y"],
            end_x=data["end_x"],
            end_y=data["end_y"],
            driver=car.driver,
            car=car,
            user_name=data["user_name"],
            fare=get_fare(data),
            distance=get_distance(data),
            estimated_time=get_estimated_time(data),

        )
        if not created:
            return {"Duplicate Rides Not Allowed"}

        serial_resp = RideSerializer(obj)
        return serial_resp.data



    def get_nearest_car(self, data):
        allcars = Car.objects.filter(booked=False)
        min_dist = float("inf")
        selected_car = None
        for i in allcars:
            dist = math.sqrt((data["start_x"] - i.current_x) ** 2 + (data["start_y"] - i.current_y) ** 2)
            if min_dist > dist or min_dist is None:
                min_dist = min(min_dist, dist)
                selected_car = i
        return selected_car
