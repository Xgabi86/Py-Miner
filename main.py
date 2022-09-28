import random

print("Voulez vous miner ? [Oui/Non]")
rep1 = input()
if rep1 == "Oui":
    
    charbonT = (random.randrange(1, 3))
    charbon = str(charbonT)
    print("Vous avez miner", charbon, "charbon.")

    with open('DB1.txt', 'w') as writer:
        writer.write(charbon)
        print("DB1 Set to:")
        print(charbon)

else:
    exit