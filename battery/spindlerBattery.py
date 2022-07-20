from datetime import date
from datetime import datetime
from battery import Battery

class SpindlerBattey(Battery):
    def __init__(self, last_service_date: date, current_service_date: date):
        self.last_service_date = last_service_date
        self.current_service_date = current_service_date
    
    def needs_service(self) -> bool:
        return self.last_service_date.replace(year=self.last_service_date.year + 2) < datetime.today().date()