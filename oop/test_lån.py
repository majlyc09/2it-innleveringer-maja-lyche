import json

class Utstyr:
    def __init__(self, produkt, dato, antall_produkter, utlant=0):
        self.produkt = produkt
        self.dato = dato
        self.antall_produkter = antall_produkter
        self.utlant = utlant

    def presenter(self):
        tilgjengelig = self.antall_produkter - self.utlant
        print(f"Produkt: {self.produkt}, Dato: {self.dato}, Tilgjengelig: {tilgjengelig}, Utlånt: {self.utlant}")

    def lan_ut(self, antall):
        tilgjengelig = self.antall_produkter - self.utlant
        if antall > tilgjengelig:
            print("Feil: Ikke nok tilgjengelig utstyr!")
        elif antall <= 0:
            print("Feil: Antall må være mer enn 0.")
        else:
            self.utlant += antall
            print(f"Lånte ut {antall} stk. {self.produkt}.")

    def lever_tilbake(self, antall):
        if antall > self.utlant:
            print("Feil: Du prøver å levere tilbake mer enn det som er utlånt!")
        elif antall <= 0:
            print("Feil: Antall må være mer enn 0.")
        else:
            self.utlant -= antall
            print(f"Leverte tilbake {antall} stk. {self.produkt}.")


# --- Lagre og laste fra fil ---

def lagre_utstyr(utstyrsliste):
    data = []
    for u in utstyrsliste:
        data.append({
            "produkt": u.produkt,
            "dato": u.dato,
            "antall_produkter": u.antall_produkter,
            "utlant": u.utlant
        })
    with open("utstyr.json", "w", encoding="utf-8") as fil:
        json.dump(data, fil, indent=4)

def last_utstyr():
    try:
        with open("utstyr.json", "r", encoding="utf-8") as fil:
            data = json.load(fil)
            liste = []
            for d in data:
                liste.append(Utstyr(d["produkt"], d["dato"], d["antall_produkter"], d["utlant"]))
            return liste
    except:
        # Hvis filen ikke finnes ennå, starter vi med utstyret ditt:
        chromebook = Utstyr("Chromebook", "2023-01-15", 10)
        lenovo_thinkpad = Utstyr("Lenovo ThinkPad", "2023-02-20", 5)
        return [chromebook, lenovo_thinkpad]


# --- Hovedprogram med meny ---

utstyrsliste = last_utstyr()

while True:
    print("\n--- MENY ---")
    print("1. Vis utstyr")
    print("2. Registrer nytt utstyr")
    print("3. Lån ut utstyr")
    print("4. Lever tilbake utstyr")
    print("5. Avslutt")

    valg = input("Velg et tall (1-5): ")

    if valg == "1":
        print("\n--- UTSTYRSLISTE ---")
        for i in range(len(utstyrsliste)):
            print(f"{i + 1}. ", end="")
            utstyrsliste[i].presenter()

    elif valg == "2":
        produkt = input("Produktnavn: ")
        dato = input("Dato (ÅÅÅÅ-MM-DD): ")
        try:
            antall = int(input("Antall produkter: "))
            if antall <= 0:
                print("Feil: Antall må være større enn 0.")
            else:
                nytt_utstyr = Utstyr(produkt, dato, antall)
                utstyrsliste.append(nytt_utstyr)
                lagre_utstyr(utstyrsliste)
                print("Nytt utstyr er registrert og lagret!")
        except ValueError:
            print("Feil: Du må skrive et tall for antall.")

    elif valg == "3":
        for i in range(len(utstyrsliste)):
            print(f"{i + 1}. {utstyrsliste[i].produkt}")
        try:
            nr = int(input("Hvilket nummer vil du låne ut? ")) - 1
            antall = int(input("Hvor mange vil du låne ut? "))
            utstyrsliste[nr].lan_ut(antall)
            lagre_utstyr(utstyrsliste)
        except (ValueError, IndexError):
            print("Feil: Ugyldig valg eller tall.")

    elif valg == "4":
        for i in range(len(utstyrsliste)):
            print(f"{i + 1}. {utstyrsliste[i].produkt}")
        try:
            nr = int(input("Hvilket nummer leveres tilbake? ")) - 1
            antall = int(input("Hvor mange leveres tilbake? "))
            utstyrsliste[nr].lever_tilbake(antall)
            lagre_utstyr(utstyrsliste)
        except (ValueError, IndexError):
            print("Feil: Ugyldig valg eller tall.")

    elif valg == "5":
        print("Avslutter programmet.")
        break

    else:
        print("Ugyldig valg, prøv igjen.")