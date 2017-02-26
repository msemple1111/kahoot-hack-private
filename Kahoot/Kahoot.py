from Kahoot import kahootVariables, kahootQueue

class Kahoot:
    def __init__(self, pin):
        self.variables = kahootVariables.Variables(pin)
        self.queue = kahootQueue.kahootQueue()
        self.send = kahootSend.kahootSend()

class KahootError(Exception):
    pass
