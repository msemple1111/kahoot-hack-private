from kahoot import Kahoot, kahootError
import json
class receive:
    def __init__(self, kahootPointer):
        self.kahootPointer = kahootPointer
        self.variables = kahootPointer.variables
        self.queue = kahootPointer.queue
        self.send = kahootPointer.send
    def connect(self, r):
        try:
            response = json.loads(r.text)
            if len(response) > 0:
                for i, x in enumerate(response):
                    if x['channel'] != "/meta/connect":
                        self.queue.add(x) #Each item needs a method to run before being added to the queue
        except:
            raise KahootError('')
    def testSession(self, r):
        try:
            if (r.status_code == 404):
                return False
            print(r.text)
            print("code:",r.status_code)
            data = json.loads(r.text)
            if data['twoFactorAuth'] == False:
                chal_r = self.send.solveKahootChallenge(data['challenge'])
                self.variables.setChallenge(chal_r.text)
                self.variables.kahootSessionShift(r.headers['x-kahoot-session-token'])
                return True
            else:
                raise kahootError.kahootError('two factor not implemented')
        except Exception as e:
            print()
            raise kahootError.kahootError('receive.testSession error')
            return False
