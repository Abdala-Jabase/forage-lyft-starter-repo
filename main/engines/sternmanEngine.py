import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from engines.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on: bool):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        if self.warning_light_is_on:
            return True
        else:
            return False
