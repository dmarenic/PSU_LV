def total_euro(sati, eura):
    return sati * eura

sati = input('Radni sati: ')
sati = sati.split(' ')[0]
sati = int(sati)

eura = input('eura/h: ')
eura = eura.split(' ')[0]
eura = float(eura)

print(f"ukupno: {total_euro(sati, eura)} eura")