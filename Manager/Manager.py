from FireUnit import FireUnit
from Event import Event

import math

class Manager:
    units: list[FireUnit]
    def __init__(self):
        print("Utworzono kierownika")
        self.units = []

    def addUnit(self, unit):
        self.units.append(unit)

    def removeUnit(self, unit:'FireUnit'):
        if unit in self.units:
            self.units.remove(unit)

    def notifyUnit(self, unit:'FireUnit', firstEvent):
        unit.update(firstEvent)

    def checkUnits(self, event:'Event'):
        carNr = event.getCarNumber()

        sortedUnits = sorted(self.units, key=lambda unit: self.distanceEarth(event.getCords(), unit.getCords()))

        for unit in sortedUnits:
            if unit.NumberOfFreeCars() >= carNr:
                return [True,unit]
        
        return [False, False]

    
    def distanceEarth(self, coords1, coords2, interpolation_exponent=1):
        lat1, lon1 = coords1
        lat2, lon2 = coords2

        lat_1 = math.radians(lat1)
        lon_1 = math.radians(lon1)
        lat_2 = math.radians(lat2)
        lon_2 = math.radians(lon2)

        r = 6376.5 * 1000

        alt_1 = 0
        alt_2 = 0

        x_1 = (r + alt_1) * math.sin(lon_1) * math.cos(lat_1)
        y_1 = (r + alt_1) * math.sin(lon_1) * math.sin(lat_1)
        z_1 = (r + alt_1) * math.cos(lon_1)

        x_2 = (r + alt_2) * math.sin(lon_2) * math.cos(lat_2)
        y_2 = (r + alt_2) * math.sin(lon_2) * math.sin(lat_2)
        z_2 = (r + alt_2) * math.cos(lon_2)

        dist = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

        return dist ** interpolation_exponent