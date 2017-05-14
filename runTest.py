from kahoot import Kahoot, kahootQueue
import sys, time, random, string


verif = False
debuga = False

def main1(a):
    try:
        k = Kahoot.Kahoot(a, debug=debuga, verify=verif)
        k.connect('mike')
        k.end()
    except Exception as e:
        print(e)
        raise
    k.end()

class clients:
    def __init__(self, pin, num, pre='play', **kwargs):
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

class manageClients:
    def __init__(self, pin, maxSize=30):
        self.pin = pin
        self.maxSize = maxSize
        self.currentlyConnected = 0
        self.postName = str(random.choice(string.ascii_letters))
        self.q = kahootQueue.kahootQueue(self.maxSize)
        self.blocks = []
        self.sent = 0
    def addBlock(self, blockSize):
        c = clients(self.pin, blockSize, q=self.q, startNumber=self.sent, post=self.postName)
        c.spam()
        self.blocks.append(c)
        self.increaseSent(blockSize)
    def increaseSent(self, increaseBy):
        self.sent = self.sent + int(increaseBy)
    def addClients(self, number):
        printClientNumber(self)
        blockSizes = self.makeBlocks(number)
        for size in blockSizes:
            self.addBlock(size)
            printClientNumber(self)
    def makeBlocks(self, number):
        blockSizes = [self.maxSize for x in range(int(number/self.maxSize))]
        blockSizes.append(number%self.maxSize)
        return blockSizes
    def getConnected(self):
        connected = 0
        for block in self.blocks:
            connected = connected + block.getConnected()
        return connected
    def end(self):
        self.q.end()


def printClients(connected, t='', sent=''):
    sys.stdout.flush()
    print(connected,"clients connected   Threads:", t,"      Sent:", sent, end='\r')

def displayClientNumber(num, c):
    coned = c.getConnected()
    while coned < num:
        printClients(coned, t=str(len(c.q.threads)), sent=str(c.sent) )
        time.sleep(0.1)
        coned = c.getConnected()
        #c.topUpWorkers()
    printClients(coned)
    print("\nFully Connected")

def printClientNumber(c):
    coned = c.getConnected()
    printClients(coned, t=str(len(c.q.threads)), sent=str(c.sent) )

def makeBlocks(number, maxSize=100):
    blockSizes = [maxSize for x in range(int(number/maxSize))]
    blockSizes.append(number%maxSize)
    return blockSizes

def main2():
    num = int(sys.argv[2])
    pin = int(sys.argv[1])
    posfixName = str(sys.argv[3])
    try:
        c = clients(pin, num, post=posfixName)
        start(pin,num, c)
        # while (c.topUpPlayers() or c.topUpWorkers()):
        #     time.sleep(0.5)
    except:
        pass

def addMasterBlock(num, pin):
    m = manageClients(pin)
    m.addClients(num)
    return m

def getMasterConnected(cList):
    connected = 0
    for x in cList:
        connected = connected + x.getConnected()
    return connected

def main(num, pin):
    blockSizes = makeBlocks(num)
    masterBlocks = []
    for x in masterBlocks:
        masterBlocks.append(addMasterBlock(x, pin))
    printClients(getMasterConnected(masterBlocks))
    return masterBlocks

timeout = 4

if __name__ == '__main__':
    num = int(sys.argv[2])
    pin = int(sys.argv[1])
    #debuga = True
    verif = True
    m = addMasterBlock(num, pin)
    displayClientNumber(num, m)
    #main1(pin)



# if __name__ == '__main__':
#     num = int(sys.argv[2])
#     pin = int(sys.argv[1])
#     try:
#         masterBlocks = main(num, pin)
#         while getMasterConnected(masterBlocks) < num:
#             printClients(getMasterConnected(masterBlocks))
#     except KeyboardInterrupt:
#         pass
#         #m.end()
#     except:
#         raise

    #  while True:
    #      if (c.topUpPlayers() and c.topUpWorkers()):
    #          time.sleep(0.5)
    #c.q.end()
