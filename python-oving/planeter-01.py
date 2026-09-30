planet0 = "jorda"
planet1 = "mars"
planet2 = "jupiter"
planet3 = "venus"
planet4 = "merkur"

solsystem = [planet0,planet1,planet2,planet3,planet4]

print(solsystem)

print(solsystem[0])

print(solsystem[4])

nyplanet = "Neptun"
solsystem.append("Neptun")

print(solsystem)

print(len(solsystem))

solsystem.remove("venus")

print(solsystem)
solsystem.pop(3)
print(solsystem)


fjernetplanet = solsystem.pop(3)
print(solsystem)
print(fjernetplanet)

for planet in solsystem:
    print(planet)



