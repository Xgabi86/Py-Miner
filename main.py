import random

print("Voulez vous miner ? [Oui/Non]")
minea = input()
if minea == "Oui":
    charbonT = (random.randrange(1, 3))
    charbon = str(charbonT)
    print("Vous avez miner", charbon, "charbon.")
elif minea == "Non":
    print("N")
with open('DB1.txt', 'w') as writer:
    writer.write(charbon)
    print("DB1 Set to:")
    print(charbon)