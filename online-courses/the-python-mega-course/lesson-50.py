
phone_numbers = {'Dad': 81638004, 'Mum': 81130625}

for k,v in phone_numbers.items():
    print("{} has a phone number {}.".format(k,v))



phone_numbers = {'Dad': "+6581638004", 'Mum': "+6581130625"}

for i in phone_numbers.values():
    print(i.replace("+", "00"))