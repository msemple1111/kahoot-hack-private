from Kahoot import Kahoot
class Variables:
    def __init__(self, pin):
        self.pin = pin
        self.kahootSession = ''
        self.verify = True
    def setVerify(self, verify):
        self.verify = verify
    def setSession(self, session):
        self.kahootSession = session
