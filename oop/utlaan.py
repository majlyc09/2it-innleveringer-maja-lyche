utstyr0 = "chromebook"
utstyr1 = "lenovo thinkpad"
utstyr2 = "camera 1"
utstyr3 = "camera 2"
utstyr4 = "headset"
utstyr5 = "microphone"
utstyr6 = "projector"
utstyr7 = "speaker"

utlånsliste = [utstyr0, utstyr1, utstyr2, utstyr3, utstyr4, utstyr5, utstyr6, utstyr7]

print("Velkommen til utlånssystemet!")
print("Her er listen over tilgjengelig utstyr:")
for i, utstyr in enumerate(utlånsliste):
    print(f"{i + 1}. {utstyr}")
    


