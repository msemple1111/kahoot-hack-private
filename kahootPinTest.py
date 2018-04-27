import time, requests, queue
from kahoot import kahootQueue
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Referer':'https://kahoot.it'
    }
class queueManage:
    def __init__(self, **kwargs):
        threadSize = 30 if 'num' not in kwargs else int(kwargs['num'])
        self.q = kahootQueue.kahootQueue(threadSize) if 'q' not in kwargs else kwargs['q']
        self.results = queue.Queue()
    def add(self, workerType, *args, **kwargs):
        self.q.add(workerType, *args, **kwargs)
    def addSessionCheck(self, pin):
        self.q.add(sessionCheck,pin,self.results)


def printTestSession(pin):
    result = testSession(sendTestSession(pin))
    if result == False:
        print(pin,"Failed")
    else:
        print(pin,"=",result)

def sessionCheck(pin, resultQ):
    resultQ.put((pin, testSession(sendTestSession(pin)) ))

def get(url):
    try:
        return requests.get(url, headers=headers, verify=False)
    except requests.exceptions.ConnectionError:
        print("error in",url)
        return None

def sendTestSession(pin):
    url = getReserveUrl(pin)
    r = get(url)
    return r

def testSession(r):
    try:
        if (r.status_code == 404):
            return False
        else:
            return True
    except:
        return False

def getReserveUrl(pin):
    return 'https://kahoot.it/reserve/session/' + str(pin) + "/?"+str(getTC())

def getTC():
    return int(time.time() * 1000)

def spamTestOld(fromPin,toPin):
    for pin in range(fromPin,toPin):
        res = (pin, testSession(sendTestSession(pin)) )
        print(res)

def spamTest(fromPin,toPin):
    manage = queueManage(num=120)
    for i in range(fromPin,toPin):
        manage.addSessionCheck(i)
    print('all sent')
    manage.q.end()
    print('all recived')
    for x in range(manage.results.qsize()):
        pin, passed = manage.results.get()
        if passed:
            print("pin:",pin,"being used")

def main():
    spamTest(10000,99999)

#main()
#print(testSession(sendTestSession(10010)))
spamTest(607773,607775)
