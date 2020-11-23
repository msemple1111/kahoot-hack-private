from Kahoot import kahootError
import time, requests
class Variables:
    def __init__(self, pin, **kwargs):
        if isinstance(pin, int):
            self.pin = pin
        else:
            raise kahootError.kahootError('pin is not an int value')
        self.debugLevel = int(kwargs['debug']) if 'debug' in kwargs else 0 #1 = some, 2 = most
        self.debug = bool(self.debugLevel != 0)
        self.verify = bool(kwargs['verify']) if 'verify' in kwargs else True
        self.timeoutTime = float(kwargs['timeout']) if 'timeout' in kwargs else 2.0
        self.isUser = bool(kwargs['isUser']) if 'isUser' in kwargs else False
        self.name = ''
        self.domain = 'kahoot.it'
        self.httpSession = requests.Session()
        self.headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Referer':'https://'+self.domain
            }
        self.kahootSession = ''
        self.kahootChallenge = ''
        self.clientid = ''
        self.subId = 1
        self.ackId = 1
        self.o = 0
        self.l = 0
        self.tc = 0
        self.ts = 0
        self.connectedClient = False
        self.clientAttempted = False
        self.currentQuestion = 0
    def __str__(self):
        return ''.join('{}: {}\n'.format(key, val) for key, val in vars(self).items())
    def setVerify(self, verify):
        self.verify = bool(verify)
    def setIsUser(self, isUser):
        self.isUser = bool(isUser)
    def setKahootSession(self, session):
        self.kahootSession = str(session)
    def setPrevTcl(self, tcl):
        self.p = tcl['p']
        self.ts = tcl['ts']
        self.tc = tcl['tc']
        self.l = (self.getTC()-self.tc-self.p)/2
        self.o = self.ts -self.tc -self.l
    def setName(self, name):
        self.name = str(name)
    def setChallenge(self, chal):
        self.kahootChallenge = str(chal)
    def setConnected(self):
        self.connectedClient = True
    def setclientId(self, clientId):
        self.clientid = str(clientId)
    def increaseSubId(self):
        self.subId = self.subId + 1
        return self.subId
    def increaseAckId(self):
        self.ackId = self.ackId + 1
        return self.ackId
    def increaseCounters(self):
        self.subId = self.subId + 1
        self.ackId = self.ackId + 1
        return (self.subId),(self.ackId)
    def getUrl(self, append=''):
        return 'https://' + self.domain + "/cometd/" + str(self.pin) + "/" + self.kahootSession+"/"+append
    def getReserveUrl(self):
        return 'https://' + self.domain + "/reserve/session/" + str(self.pin) + "/?"+str(self.getTC())
    def getName(self):
        return self.name
    def getO(self):
        return int(self.o)
    def getL(self):
        return int(self.l)
    def getTC(self):
        return int(time.time() * 1000)
    def getFailed(self):
        return self.clientFailed
    def setFailed(self):
        self.clientFailed = True
    def setCurrentQuestion(self, currentQuestion):
        self.currentQuestion = int(currentQuestion) + 1
    def getCurrentQuestionNumber(self):
        return int(self.currentQuestion + 1)
