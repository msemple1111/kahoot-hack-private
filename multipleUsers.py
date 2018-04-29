class clients:
    def __init__(self, pin, **kwargs):
        pre = 'mike' if 'pre' not in kwargs else str(kwargs['pre'])
        self.baseName = str(pre) if 'post' not in kwargs else (str(pre)+str(kwargs['post']))
        tSize = 30 if 'threadSize' not in kwargs else int(kwargs['threadSize'])
        self.numClient = 0 if 'startNumber' not in kwargs else int(kwargs['startNumber'])
        self.verify = True if 'verify' not in kwargs else bool(kwargs['verify'])
        self.debug = 0 if 'debug' not in kwargs else int(kwargs['debug'])
        self.pin = pin
        self.connectedClients = 0
        threadSize = int(tSize) if (int(tSize) < 30) else 30
        self.q = kahootQueue.kahootQueue(threadSize) if 'q' not in kwargs else kwargs['q']
        self.connects = []
        if 'number' in kwargs:
            self.sendBlock(int(kwargs['number']))
    def increaseClients(self):
        self.connectedClients = self.connectedClients + 1
    def sendBlock(self, size):
        for x in range(size):
            self.sendSingle()
    def sendSingle(self):
        self.numClient = self.numClient + 1
        name = str(self.baseName) + str(self.numClient)
        k = Kahoot.Kahoot(self.pin, q=self.q, verify=self.verify, debug=self.debug)
        if self.debug:
            print("added: ",name)
        k.connect(name)
        self.connects.append(k)
    def getNumberConnected(self):
        self.connectedClients = 0
        for x in self.connects:
            if x.checkConnected():
                self.increaseClients()
        return self.connectedClients

def main():
    num = int(sys.argv[2])
    pin = int(sys.argv[1])
    c = clients(pin, number=num, debug=2)
