from kahoot import kahoot
def main():
    kahoot = Kahoot.Kahoot(56)
    kahoot.variables.setName('mike')
    print(kahoot.variables)
    seq = [(kahoot.send.test, '0')]
    for x in range(100):
        seq.append((kahoot.send.test, x+1))
    try:
        kahoot.queue.add(kahoot.send.test, 'test')
        kahoot.queue.map(seq)
    finally:
        kahoot.queue.end()

main()
