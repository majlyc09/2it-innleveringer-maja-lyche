def beregn_avstand(fart,timer):
    if timer < 0:
        raise ValueError("tid kan ikke være negativ")
    return fart * timer

def beregn_drivstoff(avstand,timer):
    return avstand * timer





