def calculate_average_x_dspam(file_name):
    try:
        with open(file_name, 'r') as file:
            values = [float(line.split(':')[1]) for line in file if line.startswith("X-DSPAM-Confidence:")]
            if values:
                print(f"Average X-DSPAM-Confidence: {sum(values) / len(values)}")
            else:
                print("Nema podataka za izračun.")
    except FileNotFoundError:
        print("Datoteka nije pronađena!")
    except Exception as e:
        print(f"Došlo je do pogreške: {e}")

# Test datoteke
print("Ime datoteke:  mbox-short.txt")
calculate_average_x_dspam("mbox-short.txt")
print("Ime datoteke:  mbox.txt")
calculate_average_x_dspam("mbox.txt")