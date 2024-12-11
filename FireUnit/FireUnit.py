from Vector import Vector2D
from Event import Event
from ColorLogger import ColorLogger
import time

class FireUnit:
    def __init__(self, name, x, y):
        print(f"Utworzono jednostke! - {name}, {x}, {y}")
        self.name = name
        self.cords = Vector2D(x,y)
        self.cars = [True, True, True, True, True]

    def getName(self):
        return self.name

    def getCords(self):
        return self.cords.getComponents()
    
    def block(self, number):
        blocked = 0
        
        for i in range(len(self.cars)):
            if self.cars[i] == True:
                self.cars[i] = False
                blocked += 1
                if blocked == number:
                    break

    def free(self, number):
        free = 0
        
        for i in range(len(self.cars)):
            if self.cars[i] == False:
                self.cars[i] = True
                free += 1
                if free == number:
                    break

    def update(self, event:'Event'):
        logger = event.getLogger()

        self.block(event.getCarNumber())
        logger.info(f"[WYSYŁA] {self.name} - {event.getCarNumber()} samochody")
        time.sleep(event.getDrivingTime())
        if event.getFalseAlarm():
            logger.info(f"[FAŁSZYWY ALRM, POWRÓT] {self.name}")
        else:
            logger.info(f"[DZIAŁANIE] {self.name}")
            time.sleep(event.getActionTime())
            logger.info(f"[POWRÓT] {self.name}")
        
        time.sleep(event.getReturnTime())
        self.free(event.getCarNumber())
        logger.info(f"[WRÓCIŁY] {self.name} - {event.getCarNumber()} samochody")

    def NumberOfFreeCars(self):
        return sum(self.cars)