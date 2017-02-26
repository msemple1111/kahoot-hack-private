from Kahoot import Kahoot, queueWorker
def main():
    #kh = Kahoot.Kahoot(55555)
    #kahootVariablesInstance = kahootVariables.Variables('56773y')
    kahoot = Kahoot.Kahoot(56)
    kahoot.variables.setName('mike')
    print(kahoot.variables)
    printt = queueWorker.queueWorker.printt

    kahoot.queue.add(kahoot.send.test, 'test')
    try:
        seq = [(kahoot.send.test, '0')]
        for x in range(100):
            seq.append((kahoot.send.test, x+1))
        kahoot.queue.map(seq)
    finally:
        kahoot.queue.end()

main()
