from Strategy import IStrategy

class StrategyMZ(IStrategy):
    def __init__(self):
        self.carsNumber = 2
    
    def execute(self):
        pass

    def getCarNumber(self):
        return self.carsNumber