try:        
    with open("filoperasjoner/galakse.txt","r") as fil:
        print(fil.read)

except FileNotFoundError: 
    print("filen finnes ikke")

try:
    planetnummer = int(input("velg planetnummer"))
except ValueError:
    print("du må skrive inn ett gyldig tall" )
else:
    print(planetnummer)