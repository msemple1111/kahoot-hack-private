import requests
from kahoot import kahootReceive, kahootError
# import os, sys, inspect
# cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"lib")))
# if cmd_subfolder not in sys.path:
#     sys.path.insert(0, cmd_subfolder)
class kahootSend:
    def __init__(self, variables):
        self.variables = variables
        self.verify = variables.verify
        self.headers = variables.headers
        self.receive = kahootReceive.receive
    def setHeaders(self, headers):
        self.headers = headers
    def getSubID(self):
        return self.variables.increaseSubID()
    def connect(self, data):
        httpSession = variables.httpSession
        subId = self.getSubID()
        url = self.variables.getUrl('connect')
        try:
            r = httpSession.post(url, data=data, headers=self.headers, verify=self.verify)
            if r.status_code != 200:
                raise kahootError(self.variables.domain+' returned http error code ' + str(r.status_code) )
        except requests.exceptions.ConnectionError:
            print(self.variables.domain+' refused the connection')
        try:
        kahootReceive.receive(response)

        except:
            raise KahootError('')
    def printTest(self):
        print()
