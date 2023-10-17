import random

# Tölvuleikur um Dreka og drekabana

def birta_titil():
    print()
    print("====================")
    print("     Drekarnir")
    print("====================")
    print()


leikmadur = {
    "Líf": 100,
    "Árás": 5
}

def bua_til_dreka():
    dreki = {
        "Líf": 100,
        "Árás": 5
    }
    return dreki

def main():
    # Birta titil
    birta_titil()
    # Búa til drekar
    dreki1 = bua_til_dreka()
    # Main game loop
    while leikmadur['Líf'] > 0:
        svar = input("Hvað viltu gera: ")
        if svar in ["x", "exit", "hætta", "bless"]:
            break
        elif svar == "árás":
            print("\"Á\" segir drekinn og missir líf")
            dreki1['Líf'] -= leikmadur['Árás'] * random.randint(0, 10)
            # dreki1["Líf"] -= 1  # stytting á: dreki1["Líf"] = dreki1["Líf"] - 1
            print(f"Drekinn er núna með {dreki1['Líf']}")
            if dreki1['Líf'] <= 0:
                print("Drekinn er dauður!")
                break
        leikmadur["Líf"] -= dreki1['Árás'] * random.randint(0, 10)
        print(f"Drekinn bítur í þig, þú hefur {leikmadur['Líf']} eftir...")
    # Enda leikin og skrá útkomu
    if leikmadur['Líf'] <= 0:
        print("Þú tapaðir!")
    print(f"Leikmaður hefur líf {leikmadur['Líf']}")
    print(f"Dreki hefur líf {dreki1['Líf']}")


if __name__ == "__main__":
    main()

