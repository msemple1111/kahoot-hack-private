from kahoot import kahootQueue, Kahoot
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
        queue.map(returnQueue())
    finally:
        queue.end()

def returnQueue():
    q = []
    for x in range(10000):
        q.append((print, str(x)))
    return q

main()
