from kahoot import Kahoot
import sys, urllib
def main():
    verif = False
    debuga = False
    pin = int(sys.argv[1])
    name = sys.argv[2]
    k = Kahoot.Kahoot(pin, verify=verif, debug=debuga)
    k.connect(name)
    k.runClient()

main()
