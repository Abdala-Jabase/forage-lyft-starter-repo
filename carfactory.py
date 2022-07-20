
from datetime import date
from car import Car
from engine.capuletEngine import CapuletEngine
from engine.willoughbyEngine import WilloughbyEngine
from engine.sternmanEngine import SternmanEngine
from battery.spindlerBattery import SpindlerBattey
from battery.nubbinBattery import NubbinBattery

class CarFactory():
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattey(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattey(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattey(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
