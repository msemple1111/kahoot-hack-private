import requests, json
from kahoot import kahootReceive, kahootError, kahootPayloads
# import os, sys, inspect
# cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"lib")))
# if cmd_subfolder not in sys.path:
#     sys.path.insert(0, cmd_subfolder)
class kahootSend:
    def __init__(self, variables):
        self.variables = variables
        self.verify = self.variables.verify
        self.headers = self.variables.headers
        self.payloads = kahootPayload.makePayloads(self.variables)
    def setHeaders(self, headers):
        self.headers = headers
    def processResponse(self, r):
        if r.status_code != 200:
            raise kahootError(self.variables.domain+' returned http error code ' + str(r.status_code) )
        try:
            return json.loads(r.text)
        except:
            raise kahootError('The response from '+ self.variables.domain +' was unparseable')
    def send(self, dataIn, urlExt=''):
        data = str(dataIn)
        httpSession = self.variables.httpSession
        url = self.variables.getUrl(urlExt)
        try:
            r = httpSession.post(url, data=dataIn, headers=self.headers, verify=self.verify)
        except requests.exceptions.ConnectionError:
            print(self.variables.domain+' refused the connection')
        return r
    def connect(self):
        data = self.payloads.connection()
        r = self.send(data, 'connect')
        return self.loadResponse(r)
    def firstConnect(self):
        data = self.payloads.firstConnection()
        r = self.send(data, 'connect')
        return self.loadResponse(r)
    def handshake(self):
        data = self.payloads.handshake()
        r = self.send(data, 'handshake')
        return self.processResponse(r)
