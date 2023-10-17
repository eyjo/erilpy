import random

# Tölvuleikur um Dreka og drekabana

def birta_titil():
    print()
    print("====================")
    print("     Drekarnir")
    print("====================")
    print()


class Player():
    def __init__(self, lif, skadi):
        self.lif = lif
        self.skadi = skadi
    
    def aras(self):
        return random.randint(0, self.skadi)
    
    def missa_lif(self, skadi):
        self.lif -= skadi

leikmadur = Player(100, 10)

def main():
    # Birta titil
    birta_titil()
    # Búa til drekar
    dreki1 = Player(100, 5)
    # Main game loop
    while leikmadur.lif > 0:
        svar = input("Hvað viltu gera: ")
        if svar in ["x", "exit", "hætta", "bless"]:
            break
        elif svar in ["a", "árás"]:
            print("\"Á\" segir drekinn og missir líf")
            dreki1.missa_lif(leikmadur.aras())
            print(f"Drekinn er núna með {dreki1.lif}")
            if dreki1.lif <= 0:
                print("Drekinn er dauður!")
                break
        leikmadur.missa_lif(dreki1.aras())
        print(f"Drekinn bítur í þig, þú hefur {leikmadur.lif} eftir...")
    # Enda leikin og skrá útkomu
    if leikmadur.lif <= 0:
        print("Þú ert dauður!")
    print(f"Leikmaður hefur líf {leikmadur.lif}")
    print(f"Dreki hefur líf {dreki1.lif}")


if __name__ == "__main__":
    main()

