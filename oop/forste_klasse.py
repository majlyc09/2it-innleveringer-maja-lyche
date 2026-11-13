class Menneske:
    def __init__(self, navn, alder, yrke, hoyde):
        self.navn = navn
        self.alder = alder
        self.yrke = yrke
        self.hoyde = hoyde
    def presentere(self):
        print(self.navn)
    def bliEldre(self):
        print



ola = Menneske("Ola", 25, "lærer", 180)
Kari = Menneske("Kari", 67, "pensioner", 165)
filip = Menneske("Filip", 35, "ingeniør", 175)
maja = Menneske("Maja", 12, "elev", 150)

print(ola.alder)
print(Kari.alder)
print(filip.alder)
print(maja.alder)

ola.presentere()