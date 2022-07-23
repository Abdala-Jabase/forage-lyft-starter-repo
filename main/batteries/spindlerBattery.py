import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from batteries.battery import Battery
from datetime import date


class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self) -> bool:
        return self.last_service_date.replace(year=self.last_service_date.year + 2) < self.current_date