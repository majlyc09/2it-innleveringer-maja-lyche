utstyrsliste = []

def registrer_utstyr(navn, produkt, dato, antall_produkter):
    utstyr = {
        "navn": navn,
        "produkt": produkt,
        "dato": dato,
        "antall_produkter": antall_produkter,
    }
    utstyrsliste.append(utstyr)
    print(f"Utstyr registrert: {navn}, {produkt}, {dato}, {antall_produkter}")
    registrer_utstyr("Maja Lyche", "chromebook", "2024-06-01", 10)
    registrer_utstyr("Maja Lyche", "lenovo thinkpad", "2024-06-02", 5)

    print(utstyrsliste)
    
   