import json
class makePayloads:
    def __init__(self, variables):
        self.variables = variables
    def answer(self, choice):
        choice = int(choice)
        subId = str(self.variables.increaseSubId())
        innerdata = {"choice": choice, "meta": {"lag": 13, "device": {"userAgent": "your_mu", "screen": {"width": 1920, "height": 1080}}}}
        innerdata = json.dumps(innerdata)
        data = [{"channel": "/service/controller", "clientId": self.variables.clientid, "data": {"content": innerdata, "gameid": self.variables.pin, "host": "kahoot.it", "id": 6, "type": "message"}, "id": str(subId)}]
        return str(json.dumps(data))
    def connection(self):
        subId, ackId = self.variables.increaseCounters()
        data = [{"channel": "/meta/connect", "clientId": self.variables.clientid, "connectionType": "long-polling", "ext": {"ack": ackId, "timesync": {"l": self.variables.getL(), "o": self.variables.getO(), "tc": self.variables.getTC()}}, "id": str(subId)}]
        return str(json.dumps(data))
    def firstConnection(self):
        ackId = self.variables.increaseAckId()
        data = [{"advice": {"timeout": 0}, "channel": "/meta/connect", "clientId": self.variables.clientid, "connectionType": "long-polling", "ext": {"ack": ackId, "timesync": {"l": self.variables.getL(), "o": self.variables.getO(), "tc": self.variables.getTC()}}, "id": "6"}]
        return str(json.dumps(data))
    def handshake(self):
        ackId = self.variables.increaseAckId()
        data = [{"advice": {"interval": 0, "timeout": 60000}, "channel": "/meta/handshake", "ext": {"ack": ackId, "timesync": {"l": self.variables.getL(), "o": self.variables.getO(), "tc": self.variables.getTC()}}, "id": "2", "minimumVersion" : "1.0", "supportedConnectionTypes": ["long-polling"], "version": "1.0"}]
        return str(json.dumps(data))
    def subscribe(self, service, chan):
        subId = self.variables.increaseSubId()
        data = [{"channel": "/meta/"+str(chan), "clientId": self.variables.clientid, "ext": {"timesync": {"l": self.variables.getL(), "o": self.variables.getO(), "tc": self.variables.getTC()}}, "id": str(subId), "subscription": "/service/" + str(service)}]
        return str(json.dumps(data))
    def name(self):
        name = self.variables.getName()
        subId = str(self.variables.increaseSubId())
        data = [{"channel": "/service/controller", "clientId": self.variables.clientid, "data": {"gameid": self.variables.pin, "host": self.variables.domain, "name": str(name), "type": "login"}, "id": subId }]
        return str(json.dumps(data))
