from kahoot import kahootVariables, kahootQueue, kahootSend

class Kahoot:
    def __init__(self, pin):
        self.variables = kahootVariables.Variables(pin)
        self.queue = kahootQueue.kahootQueue()
        self.send = kahootSend.kahootSend(self.variables)
    def setQueue(self, queuePointer):
        self.queue.end()
        self.queue = queuePointer
    def end(self):
        self.queue.end()
        
class kahootError(Exception):
    pass
