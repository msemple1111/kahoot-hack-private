import requests, json, urllib.parse, time
from kahoot import kahootReceive, kahootPayload, kahootError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# import os, sys, inspect
# cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"lib")))
# if cmd_subfolder not in sys.path:
#     sys.path.insert(0, cmd_subfolder)
class kahootSend:
    def __init__(self, kahoot):
        self.kahoot = kahoot
        self.variables = self.kahoot.variables
        self.headers = self.variables.headers
        self.payloads = kahootPayload.makePayloads(self.variables)
        if not self.variables.debug and not self.variables.verify:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    def setHeaders(self, headers):
        self.headers = headers
    def processResponse(self, r, statusCodePass=200):
        if r.status_code != statusCodePass:
            raise kahootError.kahootError(r.url+' returned http error code ' + str(r.status_code) )
        try:
            response = json.loads(r.text)
            for x in response:
                if "successful" in x:
                    if x["successful"] != True:
                        raise kahootError.kahootError(r.url+' returned an unsuccessful response')
                if ('ext' in x) and ('timesync' in x['ext']):
                    self.variables.setPrevTcl(x['ext']['timesync'])
            return response
        except Exception as e:
            if self.variables.debug:
                print(e)
                print(r.text)
            raise kahootError.kahootError('The response from '+ r.url +' was unparseable')
    def checkResponse(self, r, statusCodePass=200, statusCodeFail=0):
        if r == None:
            raise kahootError.kahootError(self.variables.domain+' returned nothing' )
        if (r.status_code != statusCodePass) and (r.status_code != statusCodeFail):
            raise kahootError.kahootError(self.variables.domain+' returned http error code ' + str(r.status_code) )
        return r
    def send(self, dataIn, urlExt=''):
        data = str(dataIn)
        httpSession = self.variables.httpSession
        url = self.variables.getUrl(urlExt)
        try:
            r = httpSession.post(url, data=dataIn, headers=self.headers, verify=self.variables.verify)
            if self.variables.debug:
                print("\n\n\ndata:",dataIn,"\nText:", r.text)
            return r
        except requests.exceptions.ConnectionError:
            print(self.variables.domain+' refused the connection')
    def get(self, url):
        httpSession = self.variables.httpSession
        try:
            r = httpSession.get(url, headers=self.headers, verify=self.variables.verify)
            if self.variables.debug:
                print("\n\n\nurl:",url,"\nText:", r.text)
            return r
        except requests.exceptions.ConnectionError:
            return None
    def connect(self):
        data = self.payloads.connection()
        r = self.send(data, 'connect')
        self.kahoot.queue.add(self.connect)
        response = self.processResponse(r)
        self.kahoot.process.connect(response)
        return response
    def firstConnect(self):
        data = self.payloads.firstConnection()
        r = self.send(data, 'connect')
        self.kahoot.queue.add(self.connect)
        response = self.processResponse(r)
        self.kahoot.process.connect(response)
        return response
    def handshake(self):
        data = self.payloads.handshake()
        r = self.send(data, 'handshake')
        return self.processResponse(r)
    def subscribeOnce(self, service, channel):
        r = self.send(self.payloads.subscribe(service, channel), 'subscribe')
        return self.processResponse(r)
    def subscribe(self):
        channels_to_sub = ["subscribe", "unsubscribe", "subscribe"]
        services_to_sub = ["controller", "player", "status"]
        for channel in channels_to_sub:
            for service in services_to_sub:
                self.subscribeOnce(service, channel)
    def sessionStart(self):
        url = self.variables.getUrl()
        r = self.get(url)
        return self.checkResponse(r, 400).text
    def testSession(self):
        url = self.variables.getReserveUrl()
        r = self.get(url)
        return self.checkResponse(r, statusCodeFail=404)
    def solveKahootChallenge(self, dataChallenge):
        htmlDataChallenge = urllib.parse.quote_plus(str(dataChallenge))
        url = "http://safeval.pw/eval?code="+htmlDataChallenge
        attempt = 1
        r = self.get(url)
        while (r == None) and (attempt < 5):
            attempt = attempt + 1
            r = self.get(url)
            time.sleep(self.variables.timeoutTime)
        if r == None:
            if self.variables.debug:
                print("name:",self.variables.name ,"unsucsessful:",url)
            raise('Tried to solve the chalenge but unsucsessful after '+str(attempt)+' attemps')
        return self.checkResponse(r)
    def sendName(self):
        r = self.send(self.payloads.name())
        data = self.processResponse(r)
        self.kahoot.process.checkConnected(data)
        return data
    def sendAnswer(self, choice):
        payload = self.payloads.answer(choice)
        r = self.send(payload)
        return self.checkResponse(r, statusCodeFail=404)
