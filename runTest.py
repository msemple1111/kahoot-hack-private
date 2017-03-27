from kahoot import Kahoot

def main(a):
    try:
        k = Kahoot.Kahoot(a)
        k.connect('mike')
    except Exception as e:
        print(e)
        k.end()
        raise

pin = 2165544

main(pin)
