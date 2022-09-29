import random, os, codecs

print("Voulez vous miner ?")
rep1 = input("Rep: ")
if rep1 == "":

    print("E1")
    charbonT = (random.randrange(1, 3))
    fd = "DB1.txt"
    file = open(fd, 'r')
    charbonS = file.read()
    charbon = int(charbonT) + int(charbonS)
    charbon = str(charbon)
    print("Vous avez miner", int(charbonT), "charbon.")

    with open('DB1.txt', 'w') as writer:
        writer.write(charbon)
        os.close(2)
    
    del(rep1)
    del(charbonT)
    del(charbonS)
    del(charbon)

    os.system("main.py")

else:
  os.system("main.py")