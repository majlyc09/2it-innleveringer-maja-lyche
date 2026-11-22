class Romfartoy:
    def __init__(self, navn, hastighet, drivstoff):
        self.navn = navn
        self.hastighet = hastighet      
        self.drivstoff = drivstoff      

    def presenter_info(self):
        print(f"Romfartøy: {self.navn}")
        print(f"  Hastighet: {self.hastighet} km/t")
        print(f"  Drivstoff: {self.drivstoff} enheter")
        print("-" * 30)

    def ok_hastighet(self, okning, drivstofforbruk):
        
        if drivstofforbruk > self.drivstoff:
            print(f"ADVARSEL: {self.navn} har ikke nok drivstoff til denne manøveren! (Mangler {drivstofforbruk - self.drivstoff} enheter)")
        elif okning <= 0 or drivstofforbruk < 0:
            print("Ugyldig verdi for hastighetsøkning eller drivstofforbruk.")
        else:
            self.hastighet += okning
            self.drivstoff -= drivstofforbruk
            print(f"{self.navn} økte hastigheten med {okning} km/t. Ny hastighet: {self.hastighet} km/t. Gjenværende drivstoff: {self.drivstoff}.")

apollo = Romfartoy("Apollo 11", 11000, 500)
voyager = Romfartoy("Voyager 1", 61500, 120)
artemis = Romfartoy("Artemis II", 0, 1000)

print("=== STARTSTATUS ===")
apollo.presenter_info()
voyager.presenter_info()
artemis.presenter_info()

print("=== HANDLIGER ===")
artemis.ok_hastighet(25000, 400)   
apollo.ok_hastighet(3000, 150)     
voyager.ok_hastighet(5000, 200)   

print("\n=== SLUTTSTATUS ===")
apollo.presenter_info()
voyager.presenter_info()
artemis.presenter_info()