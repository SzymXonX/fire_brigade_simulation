from Strategy import IStrategy

class StrategyPZ(IStrategy):
    def __init__(self):
        self.carsNumber = 3
    
    def execute(self):
        pass

    def getCarNumber(self):
        return self.carsNumber