from datetime import date
from datetime import datetime
from car import Car
from engines.capuletEngine import CapuletEngine
from engines.willoughbyEngine import WilloughbyEngine
from engines.sternmanEngine import SternmanEngine
from batteries.spindlerBattery import SpindlerBattery
from batteries.nubbinBattery import NubbinBattery
from carfactory import CarFactory

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 3)
warning_light_is_on = False

car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)
print(car.needs_service())