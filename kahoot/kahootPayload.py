import json
class makePayloads:
    def __init__(self, variables):
        self.variables = variables
    def connection(self):
        subId, ackId = self.variables.increaseCounters()
        data = [{"channel": "/meta/connect", "clientId": self.clientid, "connectionType": "long-polling", "ext": {"ack": ackId, "timesync": {"l": self.variables.l(), "o": self.variables.o(), "tc": self.variables.getTC()}}, "id": str(subId)}]
        return str(json.dumps(data))
    def connection(self):
        ackId = self.variables.increaseAckId()
        data = [{"advice": {"timeout": 0}, "channel": "/meta/connect", "clientId": self.clientid, "connectionType": "long-polling", "ext": {"ack": ackId, "timesync": {"l": self.variables.l(), "o": self.variables.o(), "tc": self.variables.getTC()}}, "id": "6"}]
        return str(json.dumps(data))
    def handshake(self):
        ackId = self.variables.increaseAckId()
        data = [{"advice": {"interval": 0, "timeout": 60000}, "channel": "/meta/handshake", "ext": {"ack": ackId, "timesync": {"l": self.variables.l(), "o": self.variables.o(), "tc": self.variables.getTC()}}, "id": "2", "minimumVersion" : "1.0", "supportedConnectionTypes": ["long-polling"], "version": "1.0"}]
        return str(json.dumps(data))
    def subscibe(self, chan):
        subId = self.variables.increaseSubId()
        data = [{"channel": "/meta/"+str(chan), "clientId": self.clientid, "ext": {"timesync": {"l": get_l(), "o": get_o(), "tc": get_tc()}}, "id": str(subId), "subscription": "/service/subscribe"}]
        return str(json.dumps(data))
