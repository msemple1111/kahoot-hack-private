import Kahoot
class Variables:
    def __init__(self, pin):
        if isinstance(pin, int):
            self.pin = pin
        else:
            raise KahootError('pin is not an int value')
        self.verify = True
    def __str__(self):
        return ''.join('{}: {}\n'.format(key, val) for key, val in vars(self).items())
    def setVerify(self, verify):
        self.verify = bool(verify)
    def setSession(self, session):
        self.kahootSession = str(session)
    def setName(self, name):
        self.name = str(name)
