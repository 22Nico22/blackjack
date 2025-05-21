import random
print("Blackjack játék")
jatekmod = input("Barát vagy Gép ellen szerenél játszani ?: ")

def npc():
    jatekos = []
    jatekos.append(random.randint(2, 11))
    jatekos.append(random.randint(2, 11))
    jatekosdb = len(jatekos)
    jatekosertek = sum(jatekos)
    print(jatekos)
    kartyahuzas = input("Szeretnél kártyát húzni ?: ")
    if kartyahuzas.lower() == "igen":
        jatekos.append(random.randint(2, 11))
        jatekosdb = len(jatekos)
        jatekosertek = sum(jatekos)
    print(f"Összesen: {jatekosertek}")
    print(f"Játékos lapjainak darab száma: {jatekosdb}")
    print("")
    print("Npc lapjai:")
    npc = []
    npc.append(random.randint(2, 8))
    npc.append(random.randint(2, 8))
    print(npc)
    npcertek = sum(npc)
    npcdb = len(npc)
    print(f"Gép lapjai: {npcertek}")
    print(f"Gép lapjainak darab száma: {npcdb}")
    print("")
    return jatekosertek, npcertek



def embervsember():
    print("1. játékos lapjai:")
    egyjatekos = []
    egyjatekos.append(random.randint(2, 11))
    egyjatekos.append(random.randint(2, 11))
    egyjatekosertek = sum(egyjatekos)
    egyjatekosdb = len(egyjatekos)
    print(egyjatekos)
    kartyahuzas = input("Szeretnél kártyát húzni ?")
    if kartyahuzas.lower() == "igen":
        egyjatekos.append(random.randint(2, 11))
        egyjatekosertek = sum(egyjatekos)
        egyjatekosdb = len(egyjatekos)
    print(f"Összege: {egyjatekos}")
    print(f"Játékos 1 lapjainak száma: {egyjatekosdb}")
    print("")
    kettojatekos = []
    kettojatekos.append(random.randint(2, 11))
    kettojatekos.append(random.randint(2, 11))
    kettojatekosertek = sum(egyjatekos)
    kettojatekosdb = len(kettojatekos)
    print(kettojatekos)
    kartyahuzasketto = input("Szeretnél kártyát húzni ?")
    if kartyahuzas.lower() == "igen":
        kettojatekos.append(random.randint(2, 11))
        kettojatekosertek = sum(egyjatekos)
        kettojatekosdb = len(kettojatekos)
    print(f"Összege: {kettojatekosertek}")
    print(f"Játékos 2 lapjainak száma: {kettojatekosdb}")
    print("")
    return egyjatekosertek, kettojatekosertek

if jatekmod == "Gép":
    jatekosertek, npcertek = npc()
    if jatekosertek > 21:
        print("A gép nyerte!")
    elif npcertek > 21:
        print("Játékos nyerte!")
    elif jatekosertek > npcertek:
        print("Játékos nyerte!")
    else:
        print("Gép nyerte!")
elif jatekmod.lower() == "Barát":
    egyjatekosertek, kettojatekosertek = embervsember()
    if egyjatekosertek > 21:
        print("A játékos 2 nyerte!")
    elif kettojatekosertek > 21:
        print("A játékos 1 nyerte!")
    elif egyjatekosertek > kettojatekosertek:
        print("Játékos 1 nyerte!")
    elif egyjatekosertek < kettojatekosertek:
        print("Játékos 2 nyerte!")

else:
    print("Nem megfelelő játékmódot adtál meg!")