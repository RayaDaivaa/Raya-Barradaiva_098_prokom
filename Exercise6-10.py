favorite_numbers = {
    'barra': [7, 10, 11],
    'juna': [5, 12],
    'rafi': [3, 8, 20],
    'niel': [9, 11],
    'aca': [2, 6, 14]}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers:")
    for number in numbers:
        print(number)