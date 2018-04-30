from src.Booking import Booking
from src.Car import *

class CarRentalSystem:
    def __init__(self):
        self._cars = []
        self._customers = []
        self._bookings = []

    def car_search(self, name=None, model=None):
        cars = []
        for car in self._cars:
            if car.get_name() == name and car.get_model() == model:
                cars.append(car)
        return cars

    def make_booking(self, customer, period, car, location):
        new_booking = Booking(customer, period, car, location)
        self._bookings.append(new_booking)
        car.add_booking(new_booking)
        return new_booking

    def get_customer(self, username):
        """
        Just returns the first customer, should do a search but not
        needed for this use case. Will break if no customers in list
        """
        return self._customers[0]

    def add_car(self, car):
        self._cars.append(car)

    def new_customer(self, customer):
        self._customers.append(customer)

    def validate_login(self, username, password):
        for c in self._customers:
            if c.username == username and c.validate_password(password):
                return c
        return None

    def get_user_by_id(self, user_id):
        for c in self._customers:
            if c.get_id() == user_id:
                return c
        return None

    @property
    def cars(self):
        return self._cars

    def get_car(self, rego):
        for c in self._cars:
            if c.get_rego() == rego:
                return c
        return None
