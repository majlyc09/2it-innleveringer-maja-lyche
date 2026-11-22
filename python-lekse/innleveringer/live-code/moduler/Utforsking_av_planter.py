class Romfartoy:
    def __init__(self, navn, fart):
        self.navn = navn
        self.fart = fart

    def fly(self):
        print(f"{self.navn} flyr av gårde i {self.fart} km/t!")

class Mannskapsfartoy(Romfartoy):
    def __init__(self, navn, fart, astronauter):
        super().__init__(navn, fart)  
        self.astronauter = astronauter

    def land_astronauter(self):
        print(f"{self.navn} lander med {self.astronauter} astronauter.")

class Rover(Romfartoy):
    def __init__(self, navn, fart, antall_hjul):
        super().__init__(navn, fart)
        self.antall_hjul = antall_hjul

    def ta_steinprove(self):
        print(f"{self.navn} kjører på {self.antall_hjul} hjul og tar en steinprøve.")

class Satellitt(Romfartoy):
    def __init__(self, navn, fart, kamera):
        super().__init__(navn, fart)
        self.kamera = kamera

    def ta_bilde(self):
        print(f"{self.navn} tar bilde av planeten med {self.kamera}.")

fartoy1 = Mannskapsfartoy("Apollo", 30000, 3)
fartoy2 = Rover("Stifinner", 20, 6)
fartoy3 = Satellitt("Blikk", 25000, "superkamera")

fartoy1.fly()
fartoy2.fly()
fartoy3.fly()

print("---")

fartoy1.land_astronauter()
fartoy2.ta_steinprove()
fartoy3.ta_bilde()