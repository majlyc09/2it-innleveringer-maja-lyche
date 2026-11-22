class RomstasjonEnhet:
    def __init__(self, navn):
        self.navn = navn

    def utfor_oppdrag(self):
        print(f"{self.navn} er klar, men har ikke fått et spesifikt oppdrag.")

class Robot(RomstasjonEnhet):
    def utfor_oppdrag(self):
        print(f"🤖 Roboten {self.navn} reparerer solcellepanelene på utsiden av stasjonen.")


class Satellitt(RomstasjonEnhet):
    def utfor_oppdrag(self):
        print(f"🛰️ Satellitten {self.navn} sender værdata og bilder tilbake til jorden.")


class Romsonde(RomstasjonEnhet):
    def utfor_oppdrag(self):
        print(f"🔭 Romsonden {self.navn} flyr ut i verdensrommet for å måle stråling.")

enhet1 = Robot("R2-Fix")
enhet2 = Robot("Arm-01")
enhet3 = Satellitt("Vær-Sat 1")
enhet4 = Satellitt("Komm-Sat 2")
enhet5 = Romsonde("Utforsker-X")

kontrollsystem = [enhet1, enhet2, enhet3, enhet4, enhet5]

print("=== KONTROLLSYSTEM: STARTER ALLE OPPDRAG ===\n")
for enhet in kontrollsystem:
    enhet.utfor_oppdrag()