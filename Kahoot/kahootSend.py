import Kahoot
class kahootSend(Kahoot):
    def __init__(self, variables):
        self.verify = variables.verify
        self.pin = str(variables.pin)
        self.subId = 12
        self.session = variables.session
        self.headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Referer':'https://kahoot.it/'
            }
    def setHeaders(self, headers):
        self.headers = headers
    def incrementCounters(self):
        self.subId = self.subId + 1
    def connect(self, )
