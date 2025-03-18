br = []
while(True):
    try:
        num = input('Unesi broj: ')
        if num == 'Done':
            break
        br.append(float(num))
    except:
        print('Nije broj!')

print(f"Ukupno unesenih brojeva: {len(br)}")
print(f"Srednja vrijednost: {sum(br) / len(br)}")
print(f"Minimum: {min(br)}")
print(f"Maximum: {max(br)}")