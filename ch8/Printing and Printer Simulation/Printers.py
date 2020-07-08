# Creates a seperate Classes for Printing Jobs and Printers

class printJob:
    # Create an instance of a Paper with ID and Arrival Time
    def __init__(self, idNum, arrivalTime):
        self._idNum = idNum
        self._arrivalTime = arrivalTime

    # Returns the ID Number
    def idNum(self):
        return self._idNum

    # Return the arrival Time of Paper
    def arrivalTime(self):
        return self._arrivalTime


class Printer:
    # Create an instance of the Printer with the Id Number
    def __init__(self, idNum):
        self._idNum = idNum
        self._paper = None
        self.stoptime = -1

    # Determines if Printer is Free
    def isFree(self):
        return self._paper == None

    # Determine if Printer has finished a printing Job
    def isFinished(self, curTime):
        return self._paper is not None and curTime == self._stoptime

    # Prints the Job
    def print(self, paper, stoptime):
        self._paper = paper
        self._stoptime = stoptime

    # Stop Printing
    def endPrint(self):
        thepaper = self._paper
        self._paper = None
        return thepaper