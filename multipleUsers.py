class clients:
    def __init__(self, pin, pre='mike', **kwargs):
        pre = 'mike' if 'pre' not in kwargs else kwargs['pre']
        self.preName = str(pre) if 'post' not in kwargs else (str(pre)+str(kwargs['post']))
        self.num = num
        self.numClient = 0 if 'startNumber' not in kwargs else kwargs['startNumber']
        self.pin = pin
        self.connectedClients = 0
        threadSize = int(num) if (int(num)<30) else 30
        self.q = kahootQueue.kahootQueue(threadSize) if 'q' not in kwargs else kwargs['q']
        self.connects = []
    def increaseClients(self):
        self.connectedClients = self.connectedClients + 1
    def resetClients(self):
        self.connectedClients = 0
    def spammer(self):
        self.spam()
    def spam(self):
        for x in range(self.num):
            self.spamSingle()
    def topUpWorkers(self):
        while (self.q.num_worker_threads < len(self.q.threads)):
            self.q.addSingleWorkerThread()
            if self.q.num_worker_threads >= len(self.q.threads):
                return True #if we added workers
        else:
            return False #if we dont added workers
    def topUpPlayers(self):
        while (self.connectedClients<self.num):
            self.spamSingle()
            if (self.connectedClients>=self.num):
                return True #if we addded all needed players
        else:
            return False #if we dont add any players
    def spamSingle(self):
        self.numClient = self.numClient + 1
        name = str(self.preName)+str(self.numClient)
        k = Kahoot.Kahoot(self.pin,q=self.q, verify=verif, debug=debuga, timeout=timeout)
        if k.variables.debug:
            print("added: ",name)
        k.connect(name)
        self.connects.append(k)
    def connectChecker(self):
        self.resetClients()
        for x in self.connects:
            if x.checkConnected():
                self.increaseClients()
    def getConnected(self):
        self.connectChecker()
        return self.connectedClients
