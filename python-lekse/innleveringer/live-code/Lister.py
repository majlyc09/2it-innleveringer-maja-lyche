planet0 = "venus"
planet1 = "merkur"
planet2 = "jorden"
planet3 = "Mars"
planet4 = "jupiter"
planet5 = "saturn"
planet6 = "uranus"
planet7 = "neptun"


solsystem = [planet0,planet1,planet2,planet3,planet4,planet5,planet6,planet7]

print(solsystem[7])

nyplanet = "pluto"
solsystem.append(nyplanet)

print(solsystem)

solsystem.insert(1, "Aries")
print(solsystem)

solsystem.remove("pluto")
print(solsystem)

fjernetplanet = solsystem.pop(1)
print(solsystem)
print(fjernetplanet)

for planet in solsystem:
    print(planet)

for object in solsystem:
    if object == "venus":
        print(object , "eksisterer")

solsystem[2] = "Terra"
print(solsystem)

tall = (3,10,19)

for tallverdi in tall:
    print(tallverdi * 2)


for index, planet in enumerate(solsystem):
   print(index, planet)

mars = {
    "navn": "mars",
    "antall måneder": 2
}

print(mars)

planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]

planeter.remove("Venus")

fjernet_planet = planeter.pop(2)

print("planeten som ble fjernet var:", fjernetplanet)

ekspedisjon = []

planet1 = input("Hvilken planet vil du besøke? ")
planet2 = input("Hvilken planet vil du besøke? ")
planet3 = input("Hvilken planet vil du besøke? ")

ekspedisjon.append(planet1)
ekspedisjon.append(planet2)
ekspedisjon.append(planet3)

print("reiseplan:")

for planet in ekspedisjon:
    print(planet)

# Lager en tuple med de indre planetene
indre_planeter = ("Merkur", "Venus", "Jorden", "Mars")

# Skriv ut hele tuplen
print(indre_planeter)

# skriver ut elementene i indeks 1
print(indre_planeter[1])

# bruker en for-løkke for å skrive ut alle elementene i tuplen
for planet in indre_planeter:
    print(planet)

# prøver å endre mars til jupiter
# dette gir en typeerror fordi en tuple kan ikke endres etter den er opprettet
# fjern komentaren på linjen under for å teste hva som skjer
# indre_planeter[3] = "Jupiter"





