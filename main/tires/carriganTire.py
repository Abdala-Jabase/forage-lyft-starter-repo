import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from tires.tire import Tire



class CarriganTire(Tire):
    def __init__(self, list: list):
        self.list = list
    
    def needs_service(self) -> bool:
        for i in self.list:
            if i >= 0.9:
                return True
        return False