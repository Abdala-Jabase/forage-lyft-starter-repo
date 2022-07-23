import os, sys
from tokenize import Double
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from tires.tire import Tire



class OctoprimeTire(Tire):
    def __init__(self, list: list):
        self.list = list
    
    def needs_service(self) -> bool:
        sum: Double = 0
        for i in self.list:
            sum += i
            if sum >= 3:
                return True
        return False