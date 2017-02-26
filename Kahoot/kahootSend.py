import requests
# import os, sys, inspect
# cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"lib")))
# if cmd_subfolder not in sys.path:
#     sys.path.insert(0, cmd_subfolder)
class kahootSend:
    def __init__(self, variable):
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
    def test(self, testIn):
        print(testIn)
    def connect(self, data):
        pin = str(self.pin)
        while True:
            self.subId = self.subId + 1
            data = self.make_second_con_payload(self.subId)
            url = "https://kahoot.it/cometd/"+pin+"/"+self.kahoot_session+"/connect"
            try:
                r = self.s.post(url, data=data, headers=self.headers, verify=self.verify)
            if r.status_code != 200:
                error(self.subId+100, str(r.status_code)+str(r.text),False)
            except requests.exceptions.ConnectionError:
                error(self.subId+200, "Conection error",False)
                print("Connection Refused")
            try:
                response = json.loads(r.text)
                if len(response) > 0:
                    for i,x in enumerate(response):
                        if x['channel'] != "/meta/connect":
                            self.queue.append(x)
            except:
            error(12, "self.connect_while error" + str(r.text), False)
