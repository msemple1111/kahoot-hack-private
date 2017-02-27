from kahoot import kahootError
import time
class Variables:
    def __init__(self, pin):
        if isinstance(pin, int):
            self.pin = pin
        else:
            raise kahootError('pin is not an int value')
        self.verify = True
        self.kahootSession = ''
        self.name = ''
        self.domain = 'kahoot.it'
        self.httpSession = requests.Session()
        self.headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Referer':'https://kahoot.it/'
            }
        self.subId = 12
        self.ackId = 1
    def __str__(self):
        return ''.join('{}: {}\n'.format(key, val) for key, val in vars(self).items())
    def setVerify(self, verify):
        self.verify = bool(verify)
    def setSession(self, session):
        self.kahootSession = str(session)
    def setName(self, name):
        self.name = str(name)
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
    def o():
      return int(14)
    def l():
      return int(0)
    def getTC():
      return int(time.time() * 1000)
