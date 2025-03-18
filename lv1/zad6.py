def sms_analysis(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            ham_words, spam_words, spam_exclamations = 0, 0, 0
            ham_count, spam_count = 0, 0
            for line in file:
                parts = line.strip().split(None, 1)
                if len(parts) != 2:
                    continue
                label, message = parts
                word_count = len(message.split())
                if label == "ham":
                    ham_words += word_count
                    ham_count += 1
                elif label == "spam":
                    spam_words += word_count
                    spam_count += 1
                    if message.endswith("!"):
                        spam_exclamations += 1
            print(f"Prosječan broj riječi u ham porukama: {ham_words / ham_count if ham_count else 0}")
            print(f"Prosječan broj riječi u spam porukama: {spam_words / spam_count if spam_count else 0}")
            print(f"Broj spam poruka koje završavaju uskličnikom: {spam_exclamations}")
    except FileNotFoundError:
        print("Datoteka nije pronađena!")

# Test datoteke
sms_analysis("SMSSpamCollection.txt")

