person_1 = {
    'first_name': 'tiara',
    'last_name': 'putri',
    'age': '20',
    'city': 'Surakarta'}

person_2 = {
    'first_name': 'raya',
    'last_name': 'barradaiva',
    'age': '18',
    'city': 'Sukoharjo'}

person_3 = {
    'first_name': 'afifah',
    'last_name': 'nasya',
    'age': '18',
    'city': 'surakarta'}

people = [person_1, person_2, person_3]

for person in people:
    print(f"\nName: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")