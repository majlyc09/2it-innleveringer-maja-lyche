import hashlib
import secrets


brukernavn = "admin"
passord = "Mars2027"

salt = secrets.token_bytes(16)
print("salt: ", salt)

hashverdi = hashlib.sha256(salt + passord.encode()).hexdigest()
print(hashverdi)


navn = input("brukernavn: ")
passordinput = input("passord: ")

hashetinput = hashlib.sha256( salt + passordinput.encode()).hexdigest

if navn.upper() == brukernavn.upper() and passord == passordinput:
    print("innloging vellykket")
else:
    print("Feil brukernavn eller passord")

