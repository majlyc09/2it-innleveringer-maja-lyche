planet0 = "venus"
planet1 = "merkur"
planet2 = "jorden"
planet3 = "Mars"
planet4 = "jupiter"
planet5 = "saturn"
planet6 = "uranus"
planet7 = "neptun"

solsystem = ["venus","merkur"]

solsystem = [planet0,planet1,planet2,planet3,planet4,planet5,planet6,planet7]

print(solsystem[7])

nyplanet = "pluto"
solsystem.append("pluto")

print(solsystem)

solsystem.insert(1, "Aries")

print(solsystem)

solsystem.remove("pluto")
print(solsystem)

solsystem.pop(1)
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
    print(tallverdi*2)


for index, planet in enumerate(solsystem):
   print(index, planet)

mars = {
    "navn": "mars",
    "antall måneder": 2
}

print(mars)