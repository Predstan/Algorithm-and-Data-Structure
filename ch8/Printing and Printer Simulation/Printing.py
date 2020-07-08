# Printing Simulation

from Array import Array
from Queue import queue
from Printers import printJob, Printer
from random import randint

class printingSimulation:
    
    def __init__(self, numPrinters, printTime, TimeBetween, numSeconds ):
        self._arriveprob = 1.0 / TimeBetween # Probability of Arrival
        self._printTime = printTime # Priniting Time of a printer
        self._numSeconds = numSeconds # Total number of Seconds for printing
        self._served = 0 

        self._paper = queue() # Queue for Jobs to be printed
        self._printers = Array(numPrinters) # Printers Available
        for i in range(len(self._printers)):
            self._printers[i] = Printer(i+1)

        self._numPaper = 0
        self._totalWaitTime = 0

    # Run the Simulation and Prints the Result
    def run(self):
        for curTime in range(self._numSeconds + 1):
            self._handleArrival( curTime )
            self._print( curTime )
            self._stopPrint( curTime )
        self.printResult()

    # Print Result
    def printResult(self):
        avgWait = float(self._totalWaitTime)/self._served
        remaining = len(self._paper)
        print ( " number printed is  {}".format(self._served))
        print ( "Average Wait is {}".format(avgWait))
        print ( " remaining in line is {}".format(remaining))

    # Simulate arrival of Jobs to be printed
    def _handleArrival(self, curTime):
        prob = randint(0.0, 1.0)
        if prob >= 0.0 and prob <= self._arriveprob:
            paper = printJob(self._numPaper + 1, curTime)
            self._paper.enqueue( paper )
            self._numPaper += 1

    # Print a Job
    def _print(self, curTime):

        i = 0

        while i < len(self._printers):
            if self._printers[i].isFree() and not self._paper.isEmpty():
                paper = self._paper.dequeue()
                stoptime = curTime + self._printTime
                self._printers[i].print(paper, stoptime)
                self._totalWaitTime += curTime - paper._arrivalTime
                self._served += 1
            i += 1

    # Stop Printing a Job
    def _stopPrint(self, curTime):
        i = 0

        while i < len(self._printers):
            if self._printers[i].isFinished(curTime):
                self._printers[i].endPrint()
            i += 1

hey = printingSimulation(1, 2, 2, 25)
hey.run()