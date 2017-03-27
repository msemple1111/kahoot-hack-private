from kahoot import kahootVariables, kahootQueue, kahootSend, kahootReceive

class Kahoot:
    def __init__(self, pin):
        self.variables = kahootVariables.Variables(pin)
        self.queue = kahootQueue.kahootQueue()
        self.send = kahootSend.kahootSend(self.variables)
        self.receive = kahootReceive.receive(self)
    def setQueue(self, queuePointer):
        self.queue.end()
        self.queue = queuePointer
    def end(self):
        self.queue.end()
    def testSession(self):
        r = self.send.testSession()
        return self.receive.testSession(r)
    def setName(self, name):
        self.variables.setName(name)
        self.send.sendName()
    def enterSession(self):
        self.send.sessionStart()
        self.variables.processclientId(self.send.handshake())
        self.send.subscribe()
    def connect(self, name):
        try:
            if self.testSession():
                self.enterSession()
                self.setName(name)
        except Exception as e:
            print(e)
            self.end()
            raise


class kahootError(Exception):
    pass
