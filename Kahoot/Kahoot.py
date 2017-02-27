from kahoot import kahootVariables, kahootQueue, kahootSend

class Kahoot:
    def __init__(self, pin):
        self.variables = kahootVariables.Variables(pin)
        self.queue = kahootQueue.kahootQueue()
        self.send = kahootSend.kahootSend(self.variables)

class kahootError(Exception):
    pass
