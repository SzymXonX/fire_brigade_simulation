from Manager import Manager
from FireUnit import FireUnit
from Event import Event

import time
import threading
import signal
import random

class Simulation:
    events: list[Event]

    def __init__(self):
        self.addFireUnits()
        self.events = []
        self.running = True

    def signalHandler(self, sig, frame):
        print("\nZatrzymuję program...")
        self.running = False

    def addFireUnits(self):
        units = [
            ["JRG-1", 50.05995379213199, 19.943109383474667],
            ["JRG-2", 50.033365497019574, 19.935851097092094],
            ["JRG-3", 50.075724498555736, 19.88732411586945],
            ["JRG-4", 50.037722618168786, 20.00576626730511],
            ["JRG-5", 50.09184029773344, 19.919944305578543],
            ["JRG-6", 50.01614983767898, 20.01561045925575],
            ["JRG-7", 50.09411196059226, 19.97742415717613],
            ["JRG-SzkolyAspirantowPSP", 50.07716434154292, 20.032791225409188],
            ["JRG-Skawina", 49.968391115396166, 19.799524359848412],
            ["LSP-Balice", 50.078930149552995, 19.78872456123853]
        ]

        self.manager = Manager()
        for i in units:
            self.manager.addUnit(FireUnit(i[0],i[1],i[2]))

    def start(self):
        signal.signal(signal.SIGINT, self.signalHandler)

        eventThread = threading.Thread(target=self.generateEvents)
        eventThread.start()

        while self.running:
            if self.events:
                firstEvent = self.events[0]
                
                check, unit = self.manager.checkUnits(firstEvent)
                if check:
                    thread = threading.Thread(target=self.manager.notifyUnit,args=(unit, firstEvent))
                    thread.start()
                    del self.events[0]
                else:
                    time.sleep(1)

    def generateEvents(self):
        minTime, maxTime = 3,6
        eventTime = random.randint(minTime,maxTime)
        time.sleep(eventTime)
        numer = 1
        while self.running:
            for color in ["white", "red", "green", "yellow", "blue", "cyan"]:
                event = Event(numer, color)
                numer+=1
                self.events.append(event)
                
                eventTime = random.randint(minTime,maxTime)
                time.sleep(eventTime)
