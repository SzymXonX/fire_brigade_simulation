from Vector import Vector2D
from Strategy import IStrategy, StrategyPZ, StrategyMZ
from ColorLogger import ColorLogger
import random

class Event:
    strategy: IStrategy

    def __init__(self, nr, color):
        self.randomEvent()
        self.randomCords()
        self.setTimes()
        self.nr = nr
        self.color = color

        colorLogger = ColorLogger(default_color=color)
        self.logger = colorLogger.getLogger(f"[Event {nr}]")
        self.logger.info(f"Nowy Event - {self.type} - {self.getCords()}")

    def setTimes(self):
        self.drivingTime = random.randint(0, 3)
        self.actionTime = random.randint(5, 25)
        self.returnTime = random.randint(0, 3)

        if random.random() < 0.05:
            self.falseAlarm = True
        else:
            self.falseAlarm = False

    def randomEvent(self):
        if random.random() < 0.3:
            self.type = "MZ"
            self.strategy = StrategyMZ()
        else:
            self.type = "PZ"
            self.strategy = StrategyPZ()

    def randomCords(self):
        minX = 49.95855025648944
        maxX = 50.154564013341734
        minY = 19.688292482742394
        maxY = 20.02470275868903 

        self.cords = Vector2D(random.uniform(minX, maxX), random.uniform(minY, maxY))

    def getType(self):
        return self.type
        
    def getCords(self) -> list[float]:
        return self.cords.getComponents()
    
    def getDrivingTime(self):
        return self.drivingTime
    def getActionTime(self):
        return self.actionTime
    def getReturnTime(self):
        return self.returnTime
    
    def getCarNumber(self):
        return self.strategy.getCarNumber()
    def getNr(self):
        return self.nr
    def getFalseAlarm(self):
        return self.falseAlarm
    def getLogger(self):
        return self.logger