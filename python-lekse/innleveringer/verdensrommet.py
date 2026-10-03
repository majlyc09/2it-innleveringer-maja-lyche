def satelittmelding(satelittnavn,planetnavn):
    print(satelittnavn,planetnavn)

satelittmelding("Hubble","Jorda")
satelittmelding("James Webb","Mars")
satelittmelding("Voyager 1","Jupiter")

def signaltid(avstand):
    tid = avstand/300000
    return tid

print(signaltid(300000))
print(signaltid(900000))

if signaltid(300000) < 1:
    print("direkte kommunikasjon")
elif signaltid(300000) < 10:
    print("forsinket kommunikasjon")
else:
    print("stor forsinkelse")

def metiorvarsel(avstand, diameter):
    if avstand < 1000 and diameter > 1000:
        return ("høy risiko for kollisjon")
    elif avstand < 5000 and diameter > 500:
        return ("moderat risiko for kollisjon")
    else:
        return ("lav risiko for kollisjon")

meteor1 = metiorvarsel(500, 2000)
print(meteor1)

meteor2 = metiorvarsel(3000, 100)
print(meteor2)

meteor3 = metiorvarsel(6000, 600)
print(meteor3)