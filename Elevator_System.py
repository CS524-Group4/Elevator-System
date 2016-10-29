from queue import PriorityQueue

class Elevator_System:
    def __init__(self):
        self.rQueue = PriorityQueue()

    def addRequest(self, priority, data):
        self.rQueue.put(priority, data)

    def getRequest(self):
       self.rQueue._get()

    def isEmpty(self):
        if(self.rQueue.empty()):
            return True
        return False

    def getRequestSize(self):
        return self.rQueue.qsize()

    def goUP(self):
        print("up")

    def goDown(self):
        print("down")