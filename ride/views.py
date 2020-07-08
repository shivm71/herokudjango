import math
from logging import log

from rest_framework.views import APIView
from .models import Car, Ride, User
from .serializers import RideSerializer
from rest_framework.response import Response


def get_distance(data):
    return round(math.sqrt((data["start_x"] - data["end_x"]) ** 2 + (data["start_y"] - data["end_y"]) ** 2), 2)


def get_fare(data):
    base_cost = 20
    return round(base_cost + (get_distance(data) * 10), 2)


def get_estimated_time(data):
    speed = 40
    return round(get_distance(data) / speed, 2)


class Book(APIView):
    serializer_class = RideSerializer

    def post(self, request):
        data = request.data
        print(data)
        if self.validate_user(data):
            for key in data:
                if key != "user_name":
                    data[key] = float(data[key])
                    data[key] = float(data[key])

            car = self.get_nearest_car(data)
            if car is None:
                response_return = {"No Rides Available Please wait and try after some time "}
            else:
                response_return = self.book_ride(car, data)
        else:
            response_return = {"User Does not exist please register user by admin login first"}

        return Response(data=response_return, status=200)

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
        self.add_ride_to_user(obj)

        serial_resp = RideSerializer(obj)
        return serial_resp.data

    def get_nearest_car(self, data):
        all_cars = Car.objects.filter(booked=False)
        min_dist = float("inf")
        selected_car = None
        for i in all_cars:
            dist = math.sqrt((data["start_x"] - i.current_x) ** 2 + (data["start_y"] - i.current_y) ** 2)
            if min_dist > dist or min_dist is None:
                min_dist = min(min_dist, dist)
                selected_car = i
        selected_car.booked = True
        selected_car.save()
        return selected_car

    def add_ride_to_user(self, obj):
        try:
            user_entity = User.objects.get(user_name=obj.user_name)
        except:
            return False
        user_entity.rides.add(obj)
        user_entity.save()
        return True

    def validate_user(self, data):
        try:
            user_entity = User.objects.get(user_name=data["user_name"])
            return True
        except:
            return False
        pass
