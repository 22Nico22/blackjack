import random

def pontszam(kezek):
    pont = 0
    aszok = 0
    for k in kezek:
        if k[0] in ['J', 'Q', 'K']:
            pont += 10
        elif k[0] == 'A':
            pont += 11
            aszok += 1
        else:
            pont += int(k[0])
    while pont > 21 and aszok:
        pont -= 10
        aszok -= 1
    return pont

pakli = [(e, s) for s in ['♠', '♥', '♦', '♣'] for e in ['2','3','4','5','6','7','8','9','10','11']]
random.shuffle(pakli)
jatek = input("Barát ellen: B, Bot ellen: Npc, válaszod: ")
                                                    # barat ellen:
if jatek.lower() == "b":
    print("Blackjack játék - Barát ellen")

    jatekos1 = [pakli.pop(), pakli.pop()]
    jatekos2 = [pakli.pop(), pakli.pop()]

                                                            # 1
    print("\n1. játékos kezd:")
    while True:
        print("Lapjaid:", jatekos1, "Pont:", pontszam(jatekos1))
        if pontszam(jatekos1) >= 21:
            break
        valasz = input("Kérsz még lapot? (i/n): ")
        if valasz.lower() == 'i':
            jatekos1.append(pakli.pop())
        else:
            break

                                                      # 2
    print("\n2. játékos következik:")
    while True:
        print("Lapjaid:", jatekos2, "Pont:", pontszam(jatekos2))
        if pontszam(jatekos2) >= 21:
            break
        valasz = input("Kérsz még lapot? (i/n): ")
        if valasz.lower() == 'i':
            jatekos2.append(pakli.pop())
        else:
            break

    pont1 = pontszam(jatekos1)
    pont2 = pontszam(jatekos2)

    print("\n1. játékos végső lapjai:", jatekos1, "Pont:", pont1)
    print("2. játékos végső lapjai:", jatekos2, "Pont:", pont2)

    if pont1 > 21 and pont2 > 21:
        print("Mindkét játékos túllépte. Nincs nyertes.")
    elif pont1 > 21:
        print("1. játékos túllépte. 2. játékos nyert!")
    elif pont2 > 21:
        print("2. játékos túllépte. 1. játékos nyert!")
    elif pont1 > pont2:
        print("1. játékos nyert!")
    elif pont2 > pont1:
        print("2. játékos nyert!")
    else:
        print("Döntetlen!")

                                                        # bot ellen
else:
    if jatek.lower() == "npc":
        print("Blackjack játék - Npc ellen")
        jatekos = [pakli.pop(), pakli.pop()]
        npc = [pakli.pop(), pakli.pop()]

                                                            #jatekos
        print("\n1. játékos kezd:")
        while True:
            print("Lapjaid:", jatekos, "Pont:", pontszam(jatekos))
            if pontszam(jatekos) >= 21:
                break
            valasz = input("Kérsz még lapot? (i/n): ")
            if valasz.lower() == 'i':
                jatekos.append(pakli.pop())
            else:
                break
                                                               #bot
    else:
        print("Nem helyes választ adtál...")
