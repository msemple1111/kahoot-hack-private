from kahoot import kahootVariables, kahootQueue, kahootSend, kahootReceive

class Kahoot:
    def __init__(self, pin, **kwargs):
        self.queue = kwargs['q'] if 'q' in kwargs else kahootQueue.kahootQueue()
        self.variables = kahootVariables.Variables(pin, **kwargs)
        self.send = kahootSend.kahootSend(self)
        self.process = kahootReceive.receive(self)
    def setQueue(self, queuePointer):
        self.queue.end()
        self.queue = queuePointer
    def setVerify(self, verify):
        self.variables.verify = verify
    def end(self):
        self.queue.end()
    def testSession(self):
        r = self.send.testSession()
        return self.process.testSession(r)
    def setName(self, name):
        self.variables.setName(name)
        self.send.sendName()
    def enterSession(self):
        self.send.sessionStart()
    def subscribe(self):
        self.send.subscribe()
    def getClientID(self):
        r = self.send.handshake()
        self.process.processclientId(r)
    def connectTo(self, name):
        try:
            if self.testSession():
                self.enterSession()
                self.getClientID()
                self.subscribe()
                self.setName(name)
                self.send.firstConnect()
        except:
            self.variables.setFailed()
            if self.variables.debug:
                raise
    def connect(self, name):
        self.queue.add(self.connectTo,name)
    def checkConnected(self):
        return (self.variables.connectedClient)


class kahootError(Exception):
    pass
