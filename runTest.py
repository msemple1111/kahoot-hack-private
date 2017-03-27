from kahoot import Kahoot
import sys

def main(a):
    try:
        k = Kahoot.Kahoot(a)
        k.connect('mike')
        k.end()
    except Exception as e:
        print(e)
        raise
    k.end()

if __name__ == '__main__':
    pin = int(sys.argv[1])
    main(pin)
