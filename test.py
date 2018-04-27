from kahoot import kahootQueue, Kahoot, kahootReceive
import timeit
def main():
    #kh = Kahoot.Kahoot(55555)
    #kahootVariablesInstance = kahootVariables.Variables('56773y')
    kahoot = Kahoot.Kahoot(56)
    kahoot.variables.setName('mike')
    kahoot.variables.setVerify(True)
    # print(kahoot.variables)
    # print = queueWorker.queueWorker.printt

    try:
        kahoot.queue.add(print, 'test2')
    finally:
        kahoot.queue.end()
    print(kahoot.verify)

def testQueue():
    try:
        queue = kahootQueue.kahootQueue(2)
        q = returnQueue()
        queue.map(q)
    finally:
        queue.end()

def returnQueue():
    q = []
    for x in range(1000):
        q.append((print, [str(x)], {}))
    return q

def checkCompute():
    k = Kahoot.Kahoot(56)
    k.end()
    chal = "decode.call(this, 'IPou1KzjkDHK8Iv6ZOda0Ok15N1hXeKWHWUHvEq2tljWvoqWxj6YLtHrbiQOPllbTjpytp4irXyjqDaO8NTlflOvVd0MXaUwEcsX'); function decode(message) {var offset = (74 + 6 * 7 + (55 + 74 * 14 * 9)); if (this.angular.isDate(offset)) {console.log(\"Offset derived as: {\", offset, \"}\");}return _.replace(message, /./g, function(char, position) {return String.fromCharCode((((char.charCodeAt(0) * position) + offset) % 77) + 48);});}"
    k.variables.kahootChallenge = k.process.computeChallenge2(str(chal))
    session = "eyhcR0AGWx9hdQAKAQVYSVNeBHFbRkQcSQMWCCt5by4nb0cHNmEOUWRcCkZeWw4xD1ksJQMFWA8/CnwTW0cjY1wMfD1fVm4MEFFnPUN9OXQzfV5Yajw+VWsTMnthYVIM"
    k.process.solveChallenge(session)
    return k.variables.kahootSession
