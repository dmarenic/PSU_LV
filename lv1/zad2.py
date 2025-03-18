try:
    br = float(input("Unesi broj: "))
    if br < 0 or br > 1.0:
        raise ValueError("Broj mora biti izmedu 0 i 1.0!")
    if br < 0.6:
        print('F')
    elif br < 0.7:
        print('D')
    elif br < 0.8:
        print('C')
    elif br < 0.9:
        print('B')
    else:
        print('A')
except ValueError as err:
    print(err)