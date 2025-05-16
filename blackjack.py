import random
print("Blackjack játék")
jatekmod = input("Barát vagy Gép ellen szerenél játszani ?: ")

def npc():
    jatekos = []
    jatekos.append(random.randint(2, 11))
    jatekos.append(random.randint(2, 11))
    jatekosdb = len(jatekos)
    jatekosertek = sum(jatekos)
    print("jatekos")
    print(f"Összesen: {jatekosertek}")
    print(f"Játékos lapjainak darab száma: {jatekosdb}")
    print("")
    print("")
    print("Npc lapjai:")
    npc = []
    npc.append(3)
    npc.append(8)
    print(npc)
    npcertek = sum(npc)
    npcdb = len(npc)
    print(f"Gép lapjai: {npcertek}")
    print(f"Gép lapjainak darab száma: {npcdb}")

def embervsember():
    print("1. játékos lapjai:")
    egyjatekos = []
    egyjatekos.append(random.randint(2, 11))
    egyjatekos.append(random.randint(2, 11))
    egyjatekosertek = sum(egyjatekos)
    egyjatekosdb = len(egyjatekos)
    print(egyjatekos)
    print(f"Összege: {egyjatekos}")
    print(f"Játékos 1 lapjainak száma: {egyjatekosdb}")
    print("")
    print("")
    kettojatekos = []
    kettojatekos.append(random.randint(2, 11))
    kettojatekos.append(random.randint(2, 11))
    kettojatekosertek = sum(egyjatekos)
    kettojatekosdb = len(kettojatekos)
    print(kettojatekos)
    print(f"Összege: {kettojatekosertek}")
    print(f"Játékos 2 lapjainak száma: {kettojatekosdb}")

if jatekmod == "Gép":
    npc()
    if jatekosertek > 21:
        print("A gép nyerte!")
    if npcertek > 21
        print("Játékos nyerte!")
    if jatekosertek > npcertek:
        print("Játékos nyerte!")
    else:
        print("Gép nyerte!")
elif jatekmod == "Barát":
    embervsember()
    if egyjatekos > 21:
        print("A játékos 1 nyerte!")
    elif kettojatekos > 21:
        print("A játékos 2 nyerte!")
    elif egyjatekosertek > kettojatekosertek:
        print("Játékos 1 nyerte!")
    else:
        print("Játékos 2 nyerte!")

else:
    print("Nem megfelelő játékmódot adtál meg!")