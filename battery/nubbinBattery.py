from datetime import date
from datetime import datetime
from battery import Battery

class NubbinBattey(Battery):
    def __init__(self, last_service_date: date):
        self.last_service_date = last_service_date
    
    def needs_service(self) -> bool:
        self.current_date = datetime.today().date()
        return self.last_service_date.replace(year=self.last_service_date.year + 4) < self.current_date