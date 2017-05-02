from kahoot import Kahoot
def main():
    verif = False
    debuga = False
    pin = 1291508
    name = 'mike5'
    k = Kahoot.Kahoot(pin, verify=verif, debug=debuga)
    k.connect(name)

main()
