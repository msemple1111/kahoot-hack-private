from kahoot import Kahoot
import sys, urllib
def main():
    pin = int(sys.argv[1])
    name = sys.argv[2]
    k = Kahoot.Kahoot(pin, verify=False)
    k.connect(name)
    k.runClient()
try:
    main()
except:
    print('\nEnd')
