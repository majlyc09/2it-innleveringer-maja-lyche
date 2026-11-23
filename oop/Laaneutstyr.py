class Utstyr:
    def __init__(self, produkt, dato, antall_produkter):
        self.produkt = produkt
        self.dato = dato
        self.antall_produkter = antall_produkter

    def presenter(self):
        print(f"Produkt: {self.produkt}, Dato: {self.dato}, Antall produkter: {self.antall_produkter}")

import utlaan
def main():
    utstyr0 = Utstyr("chromebook", "2024-06-01", 10)
    utstyr1 = Utstyr("lenovo thinkpad", "2024-06-02", 5)
    utstyr2 = Utstyr("camera 1", "2024-06-03", 3)
    utstyr3 = Utstyr("camera 2", "2024-06-04", 2)
    utstyr4 = Utstyr("headset", "2024-06-05", 15)
    utstyr5 = Utstyr("microphone", "2024-06-06", 8)
    utstyr6 = Utstyr("projector", "2024-06-07", 1)
    utstyr7 = Utstyr("speaker", "2024-06-08", 4)

    utlånsliste = [utstyr0, utstyr1, utstyr2, utstyr3, utstyr4, utstyr5, utstyr6, utstyr7]

    print("Velkommen til utlånssystemet!")
    print("Her er listen over tilgjengelig utstyr:")
    for i, utstyr in enumerate(utlånsliste):
        print(f"{i + 1}. {utstyr.produkt} - Dato: {utstyr.dato}, Antall produkter: {utstyr.antall_produkter}")

import registrering_av_nytt_utstyr
if __name__ == "__main__":
    main()


  

