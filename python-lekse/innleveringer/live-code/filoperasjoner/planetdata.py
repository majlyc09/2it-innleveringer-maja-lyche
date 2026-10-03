#fil = open("filoperasjoner/planeter.txt","a")
#fil.write("mars\n")
#fil.close

#with open("filoperasjoner/planeter.txt","r") as fil:
    #for linje in fil:
        #print(linje.strip())

  
planet = input("skriv inn en planet")
antmåner = input("skriv inn antall måner")

with open("filoperasjoner/planeter.txt","w") as fil:
    fil.write(planet + "\n")
    fil.write(antmåner + "\n")

with open("filoperasjoner/planeter.txt","r") as fil:
    print(fil.read())

print("planeten ble lagret")

   
