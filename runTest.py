from kahoot import Kahoot
import sys

def main(a):
    try:
        k = Kahoot.Kahoot(a)
        k.connect('mike')
    except Exception as e:
        print(e)
        k.end()
        raise

if __name__ == '__main__':
    pin = sys.argv[1]
    main(pin)
