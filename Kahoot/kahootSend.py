import requests, json, urllib.parse
from kahoot import kahootReceive, Kahoot, kahootPayload, kahootError
# import os, sys, inspect
# cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"lib")))
# if cmd_subfolder not in sys.path:
#     sys.path.insert(0, cmd_subfolder)
class kahootSend:
    def __init__(self, variables):
        self.variables = variables
        self.headers = self.variables.headers
        self.payloads = kahootPayload.makePayloads(variables)
        if not self.variables.verify:
            from requests.packages.urllib3.exceptions import InsecureRequestWarning
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    def setHeaders(self, headers):
        self.headers = headers
    def processResponse(self, r, statusCodePass=200):
        if r.status_code != statusCodePass:
            raise kahootError.kahootError(self.variables.domain+' returned http error code ' + str(r.status_code) )
        try:
            response = json.loads(r.text)
            successful_flag = True
            for x in range(len(response)):
                if "successful" in response[x]:
                    if response[x]["successful"] != True:
                        raise kahootError.kahootError(self.variables.domain+' returned an unsuccessful response')
            if successful_flag:
                return response
        except:
            raise kahootError.kahootError('The response from '+ self.variables.domain +' was unparseable')
    def checkResponse(self, r, statusCodePass=200):
        if r.status_code != statusCodePass:
            raise kahootError.kahootError(self.variables.domain+' returned http error code ' + str(r.status_code) )
        return r
    def send(self, dataIn, urlExt=''):
        data = str(dataIn)
        httpSession = self.variables.httpSession
        url = self.variables.getUrl(urlExt)
        try:
            r = httpSession.post(url, data=dataIn, headers=self.headers, verify=self.variables.verify)
            print("\n\n\ndata:",dataIn,"\nText:", r.text)
            return r
        except requests.exceptions.ConnectionError:
            print(self.variables.domain+' refused the connection')
    def get(self, url):
        httpSession = self.variables.httpSession
        try:
            r = httpSession.get(url, headers=self.headers, verify=self.variables.verify)
            print("\n\n\nurl:",url,"\nText:", r.text)
            return r
        except requests.exceptions.ConnectionError:
            print(self.variables.domain+' refused the connection')
            return None
    def connect(self):
        data = self.payloads.connection()
        r = self.send(data, 'connect')
        return self.processResponse(r)
    def firstConnect(self):
        data = self.payloads.firstConnection()
        r = self.send(data, 'connect')
        return self.processResponse(r)
    def handshake(self):
        data = self.payloads.handshake()
        r = self.send(data, 'handshake')
        return self.processResponse(r)
    def subscribeOnce(self, text):
        r = self.send(self.payloads.subscribe(text), 'subscribe')
        return self.processResponse(r)
    def subscribe(self):
        subscribe_text = ["controller", "player", "status"]
        for x in subscribe_text:
            self.subscribeOnce(x)
    def sessionStart(self):
        url = self.variables.getUrl()
        r = self.get(url)
        return self.checkResponse(r, 400).text
    def testSession(self):
        url = self.variables.getReserveUrl()
        r = self.get(url)
        return self.checkResponse(r)
    def solveKahootChallenge(self, dataChallenge):
        htmlDataChallenge = urllib.parse.quote_plus(str(dataChallenge))
        url = "http://safeval.pw/eval?code="+htmlDataChallenge
        r = self.get(url)
        return r
    def sendName(self):
        r = self.send(self.payloads.name())
        print(r.text)
        return self.processResponse(r)
