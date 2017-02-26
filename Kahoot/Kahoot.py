from Kahoot import kahootVariables

class Kahoot:
    def __init__(self, pin):
        self.variables = kahootVariables.Variables(pin)

class KahootError(Exception):
    pass
